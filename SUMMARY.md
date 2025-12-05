# 📋 Récapitulatif du Projet - Portail NSI

## 🎯 Vue d'ensemble

**Portail d'apprentissage NSI** - Plateforme éducative complète pour l'enseignement de la spécialité NSI (Numérique et Sciences Informatiques) au lycée.

### Caractéristiques principales

✅ **Gestion des utilisateurs** : 3 rôles (Élève, Professeur, Admin)  
✅ **Système de classes** : Codes d'inscription, gestion des élèves  
✅ **Cours structurés** : Première et Terminale  
✅ **Exercices interactifs** : Python, SQL, QCM, Parsons  
✅ **Exécution client-side** : Pyodide (Python) et sql.js (SQL)  
✅ **Gamification** : XP, niveaux, badges, succès, classement  
✅ **Suivi pédagogique** : Dashboard professeur avec statistiques  
✅ **Interface moderne** : Tailwind CSS, HTMX  

---

## 📁 Structure du projet

```
C:/dev/NSI_portal/
│
├── 📂 nsi_project/              # Configuration Django
│   ├── settings.py              # Configuration principale
│   ├── urls.py                  # Routage principal
│   ├── wsgi.py / asgi.py        # Points d'entrée WSGI/ASGI
│
├── 📂 accounts/                 # Gestion des utilisateurs
│   ├── models.py                # User, Classroom, Enrollment
│   ├── views.py                 # Login, register, profile
│   ├── forms.py                 # Formulaires d'inscription
│   ├── admin.py                 # Interface admin
│   ├── urls.py                  # URLs de l'app
│   ├── 📂 templates/            # Templates HTML
│   ├── 📂 templatetags/         # Custom template tags
│   └── 📂 management/commands/  # create_sample_data.py
│
├── 📂 courses/                  # Gestion des cours
│   ├── models.py                # Course, Chapter, ContentBlock
│   ├── views.py                 # Liste/détail cours et chapitres
│   ├── admin.py                 # Interface admin
│   ├── urls.py                  # URLs de l'app
│   └── 📂 templates/            # Templates HTML
│
├── 📂 exercises/                # Gestion des exercices
│   ├── models.py                # Exercise, Attempt, Hint
│   ├── views.py                 # Détail exercice, soumission
│   ├── admin.py                 # Interface admin
│   ├── urls.py                  # URLs de l'app
│   └── 📂 templates/            # Templates HTML
│
├── 📂 gamification/             # Système de gamification
│   ├── models.py                # Badge, Achievement, Streak
│   ├── views.py                 # Badges, leaderboard
│   ├── utils.py                 # check_and_award_badges()
│   ├── admin.py                 # Interface admin
│   ├── urls.py                  # URLs de l'app
│   └── 📂 templates/            # Templates HTML
│
├── 📂 templates/                # Templates globaux
│   ├── base.html                # Template de base
│   ├── home.html                # Page d'accueil
│   └── dashboard.html           # Dashboard utilisateur
│
├── 📂 static/                   # Fichiers statiques
│   ├── 📂 css/                  # custom.css
│   └── 📂 js/                   # code_execution.js
│
├── 📂 media/                    # Fichiers uploadés (vide au départ)
│
├── 📄 manage.py                 # Commandes Django
├── 📄 requirements.txt          # Dépendances Python
├── 📄 .env.example              # Variables d'environnement exemple
├── 📄 .gitignore                # Fichiers ignorés par Git
│
├── 📄 README.md                 # Documentation principale
├── 📄 INSTALLATION.md           # Guide d'installation détaillé
├── 📄 QUICKSTART.md             # Guide de démarrage rapide
├── 📄 DEPLOYMENT.md             # Guide de déploiement production
├── 📄 EXERCISES_LIBRARY.md      # Bibliothèque d'exercices
│
├── 📄 start.ps1                 # Script de démarrage automatique
└── 📄 test.ps1                  # Script de test
```

---

## 🗃️ Modèles de données

### accounts.User (Custom User)
```python
- username, email, password (hérités)
- role: STUDENT / TEACHER / ADMIN
- pseudo: Pseudonyme public
- xp: Points d'expérience
- level: Niveau (calculé automatiquement)
- avatar: Image de profil
```

### accounts.Classroom
```python
- name: Nom de la classe
- school_name: Nom de l'établissement
- teacher: ForeignKey(User) [Professeur]
- join_code: Code unique à 6 caractères
- students: ManyToMany(User) via Enrollment
```

### courses.Course
```python
- title: Titre du cours
- description: Description
- level: PREMIERE / TERMINALE
- icon: Emoji représentant le cours
- order: Ordre d'affichage
- is_published: Publié ou brouillon
```

### courses.Chapter
```python
- course: ForeignKey(Course)
- title: Titre du chapitre
- slug: URL-friendly identifier
- description: Description
- order: Ordre d'affichage
- is_published: Publié ou brouillon
```

### exercises.Exercise
```python
- chapter: ForeignKey(Chapter)
- title: Titre de l'exercice
- type: PYTHON / SQL / MCQ / PARSONS
- statement_markdown: Énoncé en Markdown
- starter_code: Code de départ
- tests_definition: JSON avec les tests
- xp_reward: XP gagnés à la réussite
- order: Ordre d'affichage
- is_published: Publié ou brouillon
```

### exercises.Attempt
```python
- exercise: ForeignKey(Exercise)
- user: ForeignKey(User)
- submitted_code: Code soumis
- score: Score obtenu (0-100)
- passed: Boolean (réussi ou non)
- xp_earned: XP gagnés
- submitted_at: Date de soumission
```

### gamification.Badge
```python
- name: Nom du badge
- code: Code unique
- description: Description
- icon: Emoji du badge
- xp_requirement: XP requis pour débloquer
- order: Ordre d'affichage
- is_active: Actif ou non
```

### gamification.Achievement
```python
- name: Nom du succès
- code: Code unique
- description: Description
- icon: Emoji du succès
- xp_reward: XP gagnés au déblocage
```

---

## 🔑 Fonctionnalités clés

### 1. Système d'authentification

- **Inscription élève** : Pseudo, mot de passe
- **Inscription professeur** : Email, nom, prénom, établissement
- **Connexion** : Username ou email + mot de passe
- **Gestion de profil** : Modifier informations, avatar

### 2. Gestion des classes (Professeurs)

- **Créer une classe** : Génère un code unique à 6 caractères
- **Partager le code** avec les élèves
- **Voir les élèves inscrits** avec leurs statistiques
- **Assigner des chapitres** à la classe
- **Suivre la progression** individuelle et globale

### 3. Rejoindre une classe (Élèves)

- **Entrer le code de classe** fourni par le professeur
- **Inscription automatique** dans la classe
- **Accès aux chapitres assignés**

### 4. Parcourir les cours

- **Liste des cours** par niveau (Première/Terminale)
- **Progression** affichée pour chaque cours
- **Chapitres** avec sections de contenu
- **Navigation** entre chapitres

### 5. Faire des exercices

- **Éditeur de code** intégré (textarea)
- **Exécution Python** dans le navigateur (Pyodide)
- **Exécution SQL** dans le navigateur (sql.js)
- **Tests automatisés** avec résultats détaillés
- **Indices** progressifs (coût en XP)
- **Soumission** avec calcul du score
- **Historique** des tentatives

### 6. Gamification

- **XP** : Gagnés en réussissant des exercices
- **Niveaux** : Montée automatique (100 XP par niveau)
- **Badges** : Débloqués selon l'XP total
- **Succès** : Débloqués pour actions spécifiques
- **Classement** : Par classe, par période
- **Streaks** : Séries de connexions quotidiennes

### 7. Dashboard

**Élève :**
- XP et niveau actuel
- Progression vers le niveau suivant
- Exercices réussis / tentatives
- Taux de réussite
- Classes inscrites
- Activité récente

**Professeur :**
- Nombre total d'élèves
- Tentatives d'exercices
- Taux de réussite moyen
- Classes gérées
- Statistiques par classe

---

## 🛠️ Technologies utilisées

### Backend
- **Django 5.0** : Framework web Python
- **PostgreSQL** : Base de données relationnelle
- **Python 3.10+** : Langage de programmation

### Frontend
- **Tailwind CSS** : Framework CSS utility-first
- **HTMX 1.9.10** : Interactions dynamiques
- **Pyodide 0.24.1** : Python WebAssembly
- **sql.js 1.8.0** : SQLite WebAssembly
- **Font Awesome 6.4.0** : Icônes

### Outils de développement
- **Git** : Contrôle de version
- **VSCode** : Éditeur recommandé
- **PowerShell** : Scripts d'automatisation

### Production
- **Gunicorn** : Serveur WSGI
- **Nginx** : Serveur web / proxy inverse
- **Supervisor** : Gestion des processus
- **Let's Encrypt** : Certificats SSL gratuits

---

## 🚀 Commandes importantes

### Développement

```powershell
# Démarrage automatique
.\start.ps1

# Démarrage manuel
.\venv\Scripts\Activate.ps1
python manage.py runserver

# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Créer des données de test
python manage.py create_sample_data

# Lancer les tests
python manage.py test
# ou
.\test.ps1

# Collecter les fichiers statiques
python manage.py collectstatic

# Shell Django
python manage.py shell
```

### Production

```bash
# Déployer une nouvelle version
./deploy.sh

# Redémarrer Gunicorn
sudo supervisorctl restart nsi_portal

# Voir les logs
tail -f logs/gunicorn.log
tail -f logs/gunicorn_error.log

# Sauvegarde de la base de données
./backup_db.sh
```

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| `README.md` | Vue d'ensemble du projet, features, architecture |
| `INSTALLATION.md` | Installation détaillée, configuration PostgreSQL |
| `QUICKSTART.md` | Démarrage rapide en 5 minutes, premiers pas |
| `DEPLOYMENT.md` | Déploiement production, Nginx, SSL, sécurité |
| `EXERCISES_LIBRARY.md` | Exemples d'exercices prêts à l'emploi |
| `SUMMARY.md` | Ce fichier - récapitulatif complet |

---

## 👥 Comptes de test

Après avoir exécuté `python manage.py create_sample_data` :

| Rôle | Identifiant | Mot de passe |
|------|-------------|--------------|
| Admin | `admin` | `admin123` |
| Professeur | `prof_martin` | `prof123` |
| Élève | `eleve_alice` | `eleve123` |

**Code de classe généré** : Affiché dans la console après création

---

## 🎨 Personnalisation

### Changer les couleurs

Modifiez les classes Tailwind dans les templates :
- `bg-blue-600` → `bg-purple-600`
- `text-blue-600` → `text-purple-600`

### Ajouter un type d'exercice

1. `exercises/models.py` : Ajouter dans `ExerciseType`
2. `static/js/code_execution.js` : Ajouter la logique d'exécution
3. `templates/exercises/exercise_detail.html` : Adapter l'UI

### Ajouter un badge

Via l'admin Django ou en Python :
```python
Badge.objects.create(
    name='Platine',
    code='PLATINUM',
    description='Atteindre 2000 XP',
    icon='💎',
    xp_requirement=2000,
    is_active=True
)
```

### Ajouter un succès

Dans `gamification/utils.py` :
```python
def check_achievements(user):
    # ... code existant ...
    
    # Nouveau succès
    if user.attempts.filter(passed=True).count() == 50:
        achievement, created = Achievement.objects.get_or_create(
            code='FIFTY_EXERCISES',
            defaults={
                'name': 'Expert',
                'description': 'Réussir 50 exercices',
                'icon': '🏆',
                'xp_reward': 200
            }
        )
        # ... logique d'attribution ...
```

---

## 🧪 Tests

### Tests unitaires

Fichiers de tests :
- `accounts/tests.py` : Modèles User, Classroom, Enrollment
- `exercises/tests.py` : Modèles Exercise, Attempt, Hint
- `gamification/tests.py` : Modèles Badge, Achievement

Exécution :
```powershell
python manage.py test
```

### Tests manuels

1. **Inscription élève** → Créer un compte
2. **Connexion** → Se connecter
3. **Rejoindre une classe** → Entrer un code
4. **Parcourir un cours** → Voir les chapitres
5. **Faire un exercice** → Tester, soumettre
6. **Gagner des XP** → Vérifier l'augmentation
7. **Débloquer un badge** → Atteindre le seuil d'XP
8. **Voir le classement** → Comparer avec d'autres

---

## 🔐 Sécurité

### Bonnes pratiques implémentées

✅ **Authentification Django** : Sessions sécurisées  
✅ **CSRF Protection** : Tokens anti-CSRF  
✅ **Validation des entrées** : Forms Django  
✅ **Exécution client-side** : Pas de `eval()` côté serveur  
✅ **Mots de passe hashés** : PBKDF2 par défaut  
✅ **Variables d'environnement** : `.env` pour les secrets  

### Checklist production

- [ ] `DEBUG=False`
- [ ] `SECRET_KEY` aléatoire et long
- [ ] `ALLOWED_HOSTS` configuré
- [ ] HTTPS activé (Let's Encrypt)
- [ ] Firewall activé (UFW)
- [ ] Fail2ban installé
- [ ] Sauvegardes automatiques
- [ ] Mises à jour régulières

---

## 📈 Évolutions futures

### Fonctionnalités suggérées

1. **Notifications** : Alertes pour nouveaux exercices, badges
2. **Forum** : Entraide entre élèves
3. **Éditeur amélioré** : Coloration syntaxique, autocomplétion
4. **Évaluations** : Contrôles notés par le professeur
5. **Analytics** : Graphiques de progression
6. **Mobile app** : Version React Native
7. **API REST** : Pour intégrations externes
8. **Webhooks** : Intégration Discord, Slack
9. **Thème sombre** : Mode sombre
10. **Export PDF** : Générer des rapports de progression

### Optimisations techniques

- **Cache Redis** : Accélérer les requêtes
- **CDN** : Servir les fichiers statiques
- **Lazy loading** : Images et composants
- **Pagination** : Listes longues
- **Indexation DB** : Optimiser les requêtes
- **Tests E2E** : Selenium, Playwright
- **CI/CD** : GitHub Actions, GitLab CI

---

## 🆘 Support et dépannage

### Problèmes courants

**Erreur : Module 'psycopg2' not found**
```powershell
pip install psycopg2-binary
```

**Erreur : No module named 'accounts'**
```powershell
# Vérifier INSTALLED_APPS dans settings.py
```

**Migrations échouent**
```powershell
python manage.py migrate --run-syncdb
```

**CSS/JS ne se charge pas**
```powershell
python manage.py collectstatic --clear
```

**502 Bad Gateway en production**
```bash
sudo supervisorctl restart nsi_portal
sudo systemctl restart nginx
```

### Logs utiles

- **Django** : Console du serveur
- **Gunicorn** : `/home/nsi/NSI_portal/logs/gunicorn.log`
- **Nginx** : `/var/log/nginx/error.log`
- **PostgreSQL** : `/var/log/postgresql/...`

---

## 📞 Contact et contribution

### Contribuer au projet

1. **Fork** le repository
2. **Créer une branche** : `git checkout -b feature/ma-fonctionnalite`
3. **Commit** : `git commit -m "Ajout de ma fonctionnalité"`
4. **Push** : `git push origin feature/ma-fonctionnalite`
5. **Pull Request** sur le repository principal

### Signaler un bug

Ouvrez une **issue** sur GitHub avec :
- Description du problème
- Étapes pour reproduire
- Logs d'erreur
- Environnement (OS, Python, Django version)

---

## 📊 Statistiques du projet

- **Lignes de code** : ~5000+
- **Fichiers** : 60+
- **Modèles Django** : 13
- **Templates** : 15+
- **Apps Django** : 4 (accounts, courses, exercises, gamification)
- **Tests unitaires** : 20+
- **Documentation** : 5 fichiers Markdown

---

## 🎓 Licence

Ce projet est destiné à un usage éducatif. Vous pouvez l'utiliser, le modifier et le distribuer librement dans un cadre pédagogique.

---

## ✨ Remerciements

Projet créé pour l'enseignement de la spécialité **NSI** (Numérique et Sciences Informatiques) au lycée.

Merci aux technologies open-source utilisées :
- Django
- Tailwind CSS
- Pyodide
- sql.js
- Et tous les contributeurs de ces projets !

---

**Bon code et bon enseignement ! 🚀👨‍🏫👩‍🎓**
