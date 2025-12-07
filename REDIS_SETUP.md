# Configuration Redis pour NSI Portal

## Installation sur Railway

1. **Ajouter un service Redis dans Railway**
   - Cliquer sur "New" → "Database" → "Add Redis"
   - Railway va créer une instance Redis et générer automatiquement `REDIS_URL`

2. **Installer les dépendances Python**
   ```bash
   pip install django-redis redis
   ```

3. **Ajouter à `requirements.txt`**
   ```
   django-redis==5.4.0
   redis==5.0.1
   ```

## Configuration Django

### 1. Ajouter dans `nsi_project/settings_prod.py`

```python
import os

# Configuration Redis Cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True,
            },
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
        },
        'KEY_PREFIX': 'nsi_portal',
        'TIMEOUT': 300,  # 5 minutes par défaut
    }
}

# Sessions en Redis (recommandé)
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Cache template loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
```

### 2. Utiliser le cache dans les vues

```python
from django.core.cache import cache
from django.views.decorators.cache import cache_page

# Cache une vue pendant 5 minutes
@cache_page(60 * 5)
def my_view(request):
    pass

# Cache manuel
def get_courses():
    courses = cache.get('all_courses')
    if courses is None:
        courses = list(Course.objects.filter(is_published=True))
        cache.set('all_courses', courses, 300)  # 5 min
    return courses
```

### 3. Cache bas niveau pour les données fréquentes

```python
# courses/views.py
from django.core.cache import cache

class CourseListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        cache_key = 'courses_published'
        courses = cache.get(cache_key)
        
        if courses is None:
            courses = list(
                Course.objects.filter(is_published=True)
                .prefetch_related(
                    Prefetch('chapters', 
                            queryset=Chapter.objects.filter(is_published=True))
                )
            )
            cache.set(cache_key, courses, 600)  # 10 minutes
        
        return courses
```

### 4. Invalider le cache quand nécessaire

```python
# models.py
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Course)
def invalidate_course_cache(sender, instance, **kwargs):
    cache.delete('courses_published')
    cache.delete(f'course_{instance.slug}')
```

## Test de la configuration Redis

```python
# Dans le shell Django
python manage.py shell

from django.core.cache import cache

# Test écriture
cache.set('test_key', 'Hello Redis!', 300)

# Test lecture
print(cache.get('test_key'))  # Doit afficher: Hello Redis!

# Test de connexion
from django_redis import get_redis_connection
conn = get_redis_connection("default")
print(conn.ping())  # Doit afficher: True
```

## Monitoring Redis

```python
# Voir les stats Redis
from django_redis import get_redis_connection
conn = get_redis_connection("default")
info = conn.info()
print(f"Used memory: {info['used_memory_human']}")
print(f"Connected clients: {info['connected_clients']}")
print(f"Total commands: {info['total_commands_processed']}")
```

## Variables d'environnement Railway

Railway définit automatiquement :
- `REDIS_URL` : URL de connexion complète (redis://...)

Pas besoin de configuration supplémentaire !

## Stratégie de cache recommandée

### Cache long (1 heure)
- Liste des cours (`all_courses`)
- Contenu des chapitres (`chapter_content_{slug}`)
- Badges disponibles (`all_badges`)

### Cache moyen (10 minutes)
- Classement (`leaderboard_global`)
- Statistiques utilisateur (`user_stats_{id}`)

### Cache court (2 minutes)
- Progression d'un chapitre (`chapter_progress_{user_id}_{chapter_id}`)
- Tentatives récentes (`recent_attempts_{user_id}`)

### Pas de cache
- Soumission d'exercices (données temps réel)
- Informations de profil

## Commandes utiles

```bash
# Vider tout le cache
python manage.py shell -c "from django.core.cache import cache; cache.clear()"

# Voir les clés en cache
from django_redis import get_redis_connection
conn = get_redis_connection("default")
keys = conn.keys("nsi_portal:*")
print(f"Nombre de clés en cache: {len(keys)}")
```

## Impact attendu

- ⚡ **Temps de réponse** : -50% à -70%
- 📊 **Charge DB** : -60% à -80%
- 👥 **Capacité** : 3x à 5x plus d'utilisateurs simultanés
- 💾 **Mémoire Redis** : ~50-100 MB pour 1000 utilisateurs

## Coût

- **Railway Redis** : ~$5/mois pour 512 MB
- **Alternative** : Redis Cloud (gratuit jusqu'à 30 MB)

## Troubleshooting

### Erreur de connexion Redis
```python
# Vérifier si Redis est accessible
import redis
try:
    r = redis.from_url(os.environ.get('REDIS_URL'))
    r.ping()
    print("✅ Redis connecté")
except Exception as e:
    print(f"❌ Erreur Redis: {e}")
```

### Fallback sans Redis
```python
# Dans settings_prod.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```

## Prochaines étapes

1. ✅ Installer Redis sur Railway
2. ✅ Ajouter configuration dans settings_prod.py
3. ✅ Tester la connexion
4. 🔄 Ajouter cache sur vues principales
5. 📊 Monitorer les performances
