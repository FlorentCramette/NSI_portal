# 🚀 Performance et Scalabilité - Portail NSI

## 📊 Analyse de la capacité actuelle

### ✅ Points forts existants

1. **Architecture client-side** 
   - ✅ Pyodide et sql.js s'exécutent dans le navigateur
   - ✅ Pas de charge serveur pour l'exécution de code
   - ✅ Réduit drastiquement la charge CPU/mémoire côté serveur

2. **Base de données optimisée**
   - ✅ PostgreSQL avec pooling de connexions (`conn_max_age=600`)
   - ✅ `select_related()` utilisé dans les vues principales
   - ✅ Index sur les clés étrangères

3. **Configuration production**
   - ✅ Gunicorn avec 3 workers par défaut
   - ✅ WhiteNoise pour les fichiers statiques
   - ✅ Timeout de 120s

### ⚠️ Points à améliorer pour 50+ utilisateurs simultanés

## 🎯 Optimisations recommandées

### 1. **Cache Redis** (Priorité HAUTE)

**Problème actuel :** Chaque requête charge les données depuis PostgreSQL

**Solution :**
```python
# Installation
# requirements.txt
django-redis==5.4.0
redis==5.0.1

# settings_prod.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True,
            }
        },
        'KEY_PREFIX': 'nsi_portal',
        'TIMEOUT': 300,  # 5 minutes par défaut
    }
}

# Cache des sessions en Redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
```

**Impact :** Réduit de 60-80% la charge sur PostgreSQL

### 2. **Database Connection Pool** (Priorité HAUTE)

```python
# settings_prod.py
DATABASES = {
    'default': {
        # ... configuration existante ...
        'CONN_MAX_AGE': 600,  # ✅ Déjà configuré
        'OPTIONS': {
            'connect_timeout': 10,
            'options': '-c statement_timeout=30000',  # 30s timeout
        },
        # Ajouter pgbouncer en production pour pooling avancé
    }
}
```

### 3. **Optimisation des requêtes** (Priorité MOYENNE)

**Problèmes détectés :**
- Vérification des badges à chaque soumission réussie
- Pas de prefetch pour les relations many-to-many

**Solutions :**

```python
# exercises/views.py - Optimiser SubmitAttemptView
def post(self, request, pk):
    # Utiliser select_for_update pour éviter race conditions
    exercise = Exercise.objects.select_related('chapter').get(pk=pk)
    
    # Batch les vérifications de badges (faire en tâche async)
    if passed:
        from django.core.cache import cache
        
        # Vérifier si déjà gagné (cache)
        cache_key = f'user_first_pass_{user.id}_{exercise.id}'
        is_first_pass = cache.get(cache_key)
        
        if is_first_pass is None:
            is_first_pass = not exercise.attempts.filter(
                user=user, passed=True
            ).exists()
            cache.set(cache_key, is_first_pass, 3600)
```

### 4. **Gunicorn configuration avancée** (Priorité HAUTE)

```python
# start.py - Améliorer la configuration Gunicorn
workers = int(os.environ.get('WEB_CONCURRENCY', '4'))  # 2*CPU+1
worker_class = 'gthread'  # Support des threads
threads = int(os.environ.get('GUNICORN_THREADS', '2'))
worker_connections = 1000
max_requests = 1000  # Redémarrage après 1000 requêtes
max_requests_jitter = 50  # Variation aléatoire
keepalive = 5

cmd = [
    "gunicorn",
    "nsi_project.wsgi:application",
    "--bind", f"0.0.0.0:{port}",
    "--workers", str(workers),
    "--worker-class", worker_class,
    "--threads", str(threads),
    "--worker-connections", str(worker_connections),
    "--max-requests", str(max_requests),
    "--max-requests-jitter", str(max_requests_jitter),
    "--keepalive", str(keepalive),
    "--timeout", "120",
    "--access-logfile", "-",
    "--error-logfile", "-",
    "--log-level", "info",
]
```

### 5. **Compression et CDN** (Priorité MOYENNE)

```python
# settings_prod.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',  # ✅ AJOUTER
    # ... reste
]

# Compression WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Caching headers pour statiques
WHITENOISE_MAX_AGE = 31536000  # 1 an
```

### 6. **Monitoring et limites** (Priorité HAUTE)

```python
# Installation
# pip install django-ratelimit

# settings_prod.py
RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'default'

# exercises/views.py
from django_ratelimit.decorators import ratelimit

@method_decorator(ratelimit(key='user', rate='100/h', method='POST'), name='dispatch')
class SubmitAttemptView(LoginRequiredMixin, View):
    """Limite à 100 soumissions par heure par utilisateur"""
    pass
```

### 7. **Tâches asynchrones** (Priorité MOYENNE)

Pour les opérations lourdes (badges, achievements, emails) :

```python
# Installation
# pip install celery redis

# settings_prod.py
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Paris'

# Déplacer vérification badges en tâche async
from celery import shared_task

@shared_task
def check_user_badges_achievements(user_id):
    user = User.objects.get(id=user_id)
    # Vérification badges et achievements
    pass
```

## 📈 Capacité estimée avec optimisations

### Avant optimisations (état actuel)
- **10-15 utilisateurs simultanés** : ✅ OK
- **20-30 utilisateurs simultanés** : ⚠️ Possible mais lent
- **50+ utilisateurs simultanés** : ❌ Risque de timeout

**Goulets d'étranglement :**
- Connexions DB limitées
- Pas de cache
- Vérifications synchrones lourdes

### Après optimisations (avec Redis + Config Gunicorn)
- **50 utilisateurs simultanés** : ✅ OK
- **100 utilisateurs simultanés** : ✅ OK
- **200+ utilisateurs simultanés** : ⚠️ Nécessite scaling horizontal

**Configuration Railway recommandée :**
- **Postgres** : Hobby plan (1 GB RAM minimum)
- **Redis** : Instance Redis (512 MB minimum)
- **Web Service** : 1 GB RAM, 1 vCPU minimum

## 🔧 Plan d'implémentation rapide

### Phase 1 : Optimisations immédiates (30 min)
1. ✅ Augmenter workers Gunicorn à 4
2. ✅ Activer GZip compression
3. ✅ Ajouter rate limiting basique

### Phase 2 : Cache Redis (1-2h)
1. Ajouter Redis sur Railway
2. Configurer django-redis
3. Cacher les cours, chapitres, exercices
4. Sessions en Redis

### Phase 3 : Optimisation DB (1h)
1. Ajouter prefetch_related où nécessaire
2. Créer index manquants
3. Optimiser les requêtes lourdes

### Phase 4 : Tâches async (2-3h)
1. Setup Celery + Redis
2. Déplacer vérifications badges en async
3. Emails en async

## 🧪 Tests de charge recommandés

```bash
# Installer locust
pip install locust

# Créer locustfile.py
from locust import HttpUser, task, between

class NSIUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def view_courses(self):
        self.client.get("/courses/")
    
    @task(2)
    def view_chapter(self):
        self.client.get("/courses/chapter/nsi-1-python-bases/")
    
    @task(1)
    def submit_exercise(self):
        self.client.post("/exercises/1/submit/", json={
            "passed": True,
            "score": 100
        })

# Lancer le test
# locust -f locustfile.py --host=https://votre-app.railway.app
```

## 📊 Métriques à surveiller

1. **Temps de réponse moyen** : < 200ms
2. **Temps de réponse P95** : < 1s
3. **Utilisation CPU** : < 70%
4. **Utilisation RAM** : < 80%
5. **Connexions DB actives** : < 80% du pool
6. **Hit rate cache Redis** : > 80%

## 🎯 Verdict : 50 utilisateurs simultanés ?

### Configuration ACTUELLE (dev)
- **Réponse** : ❌ **NON**, risque de timeouts et lenteurs
- **Limite estimée** : 10-15 utilisateurs simultanés

### Avec optimisations MINIMALES (Phase 1 + 2)
- **Réponse** : ✅ **OUI**, confortablement
- **Capacité** : 50-100 utilisateurs simultanés

### Configuration RECOMMANDÉE pour production
```yaml
# railway.toml
[build]
builder = "DOCKERFILE"

[deploy]
startCommand = "python start.py"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10

[env]
WEB_CONCURRENCY = "4"
GUNICORN_THREADS = "2"
DJANGO_SETTINGS_MODULE = "nsi_project.settings_prod"

# Services requis
# - PostgreSQL (Hobby: $5/mo)
# - Redis (512MB: $5/mo)
# - Web Service (1GB RAM: $5/mo)
```

## ✅ Actions prioritaires MAINTENANT

1. **Ajouter Redis** - Impact immédiat maximum
2. **Optimiser Gunicorn** - Configuration simple
3. **Ajouter monitoring** - Sentry ou équivalent
4. **Rate limiting** - Protection essentielle

**Temps total d'implémentation** : 2-4 heures
**Coût mensuel Railway** : ~$15-20 avec Redis

## 📚 Ressources

- [Django Performance Tips](https://docs.djangoproject.com/en/5.0/topics/performance/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/settings.html)
- [Railway Scaling Guide](https://docs.railway.app/reference/scaling)
- [Django-Redis Documentation](https://github.com/jazzband/django-redis)
