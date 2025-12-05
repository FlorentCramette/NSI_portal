# 🚀 Guide de Démarrage Rapide - Portail NSI

## Installation

### 1. Créer un environnement virtuel

```powershell
# Ouvrir PowerShell dans le dossier du projet
cd C:\dev\NSI_portal

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1
```

### 2. Installer les dépendances

```powershell
pip install -r requirements.txt
```

### 3. Configurer PostgreSQL

**Installer PostgreSQL** (si ce n'est pas déjà fait) :
- Télécharger depuis https://www.postgresql.org/download/windows/
- Installer avec le mot de passe de votre choix pour l'utilisateur `postgres`

**Créer la base de données** :

```powershell
# Se connecter à PostgreSQL
psql -U postgres

# Dans psql, créer la base de données
CREATE DATABASE nsi_platform;

# Créer un utilisateur (optionnel)
CREATE USER nsi_user WITH PASSWORD 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE nsi_platform TO nsi_user;

# Quitter psql
\q
```

### 4. Configurer les variables d'environnement

```powershell
# Copier le fichier .env.example
cp .env.example .env

# Éditer .env avec vos paramètres
notepad .env
```

Modifier les valeurs dans `.env` :
```
SECRET_KEY=votre-clé-secrète-générée-aléatoirement
DEBUG=True
DATABASE_NAME=nsi_platform
DATABASE_USER=postgres
DATABASE_PASSWORD=votre_mot_de_passe_postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Appliquer les migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 6. Créer un superutilisateur

```powershell
python manage.py createsuperuser
```

Suivez les instructions pour créer votre compte administrateur.

### 7. Charger les données initiales (optionnel)

```powershell
# Si vous avez créé des fixtures
python manage.py loaddata initial_data.json
```

### 8. Lancer le serveur

```powershell
python manage.py runserver
```

Le site sera accessible à : **http://localhost:8000**

L'interface d'administration sera à : **http://localhost:8000/admin**

---

## 📋 Utilisation

### Pour les élèves

1. **S'inscrire** : http://localhost:8000/accounts/register/student/
   - Choisir un nom d'utilisateur et un pseudo
   - Optionnellement entrer un code de classe

2. **Rejoindre une classe** (si pas fait à l'inscription)
   - Aller dans "Rejoindre une classe"
   - Entrer le code fourni par le professeur

3. **Suivre les cours**
   - Parcourir les chapitres
   - Faire les exercices interactifs
   - Gagner des XP et des badges

### Pour les professeurs

1. **S'inscrire** : http://localhost:8000/accounts/register/teacher/
   - Fournir email professionnel et informations

2. **Créer une classe**
   - Aller dans le tableau de bord
   - Cliquer sur "Créer une classe"
   - Noter le code généré pour le partager avec les élèves

3. **Attribuer des chapitres**
   - Parcourir les cours
   - Attribuer des chapitres à vos classes

4. **Suivre la progression**
   - Voir les statistiques de chaque élève
   - Consulter les tentatives d'exercices

### Pour les administrateurs

1. **Accéder à l'interface admin** : http://localhost:8000/admin

2. **Créer du contenu**
   - Ajouter des cours (Première/Terminale)
   - Créer des chapitres
   - Ajouter des blocs de contenu (markdown)
   - Créer des exercices (Python, SQL, QCM)

3. **Gérer la gamification**
   - Créer des badges
   - Configurer des accomplissements

---

## 🎓 Créer des Exercices

### Exercice Python

Dans l'admin, créer un exercice avec :

**Type** : Python

**Code de départ** :
```python
def calculer_somme(a, b):
    # À compléter
    pass
```

**Définition des tests** (JSON) :
```json
{
  "tests": [
    {
      "name": "Test 1 : Addition simple",
      "code": "calculer_somme(2, 3)",
      "expected": 5
    },
    {
      "name": "Test 2 : Nombres négatifs",
      "code": "calculer_somme(-1, 1)",
      "expected": 0
    }
  ]
}
```

### Exercice SQL

**Type** : SQL

**Définition des tests** (JSON) :
```json
{
  "schema": "CREATE TABLE eleves (id INTEGER, nom TEXT, note INTEGER); INSERT INTO eleves VALUES (1, 'Alice', 15), (2, 'Bob', 12);",
  "tests": [
    {
      "name": "Sélectionner tous les élèves",
      "expectedQuery": "SELECT * FROM eleves WHERE note >= 10"
    }
  ]
}
```

---

## 🛠️ Commandes Utiles

```powershell
# Créer des migrations après modification des modèles
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques (pour production)
python manage.py collectstatic

# Lancer le shell Django
python manage.py shell

# Créer une nouvelle app
python manage.py startapp nom_app
```

---

## 📦 Structure du Projet

```
NSI_portal/
├── accounts/              # Gestion utilisateurs et classes
│   ├── models.py         # User, Classroom, Enrollment
│   ├── views.py          # Vues d'authentification
│   ├── forms.py          # Formulaires d'inscription
│   └── templates/        # Templates accounts
├── courses/              # Cours et chapitres
│   ├── models.py         # Course, Chapter, ContentBlock
│   ├── views.py          # Vues des cours
│   └── templates/        # Templates courses
├── exercises/            # Exercices et tentatives
│   ├── models.py         # Exercise, Attempt, Hint
│   ├── views.py          # Vues d'exercices
│   └── templates/        # Templates exercises
├── gamification/         # Badges et XP
│   ├── models.py         # Badge, Achievement, Streak
│   └── views.py          # Classement et badges
├── nsi_project/          # Configuration Django
│   ├── settings.py       # Paramètres du projet
│   └── urls.py           # URLs principales
├── static/               # Fichiers statiques
│   ├── css/             # Styles (Tailwind via CDN)
│   └── js/              # Scripts JavaScript
│       └── code_execution.js  # Pyodide & sql.js
├── templates/            # Templates globaux
│   ├── base.html        # Template de base
│   ├── home.html        # Page d'accueil
│   └── dashboard.html   # Tableau de bord
├── manage.py            # Script de gestion Django
└── requirements.txt     # Dépendances Python
```

---

## 🎨 Technologies Utilisées

- **Backend** : Django 5.0
- **Base de données** : PostgreSQL
- **Frontend** : HTML, Tailwind CSS (CDN), HTMX
- **Exécution Python** : Pyodide (WebAssembly)
- **Exécution SQL** : sql.js (SQLite en mémoire)
- **Éditeur de code** : Textarea avec coloration syntax (peut être amélioré avec Monaco/CodeMirror)

---

## 🔒 Sécurité

- **IMPORTANT** : Le code Python et SQL s'exécute **uniquement côté client** (navigateur)
- Aucun code utilisateur n'est exécuté sur le serveur
- Le serveur reçoit uniquement les résultats (passé/échoué, score)
- En production, changer `DEBUG=False` et utiliser une vraie `SECRET_KEY`

---

## 🐛 Dépannage

### Erreur de connexion PostgreSQL
- Vérifier que PostgreSQL est démarré
- Vérifier les identifiants dans `.env`
- Tester la connexion : `psql -U postgres -d nsi_platform`

### Erreur "Module not found"
- Vérifier que l'environnement virtuel est activé
- Réinstaller les dépendances : `pip install -r requirements.txt`

### Pyodide ne charge pas
- Vérifier la connexion Internet (Pyodide est chargé via CDN)
- Ouvrir la console du navigateur (F12) pour voir les erreurs

---

## 📝 TODO / Améliorations Futures

- [ ] Intégrer Monaco Editor pour une meilleure expérience de codage
- [ ] Ajouter des exercices Parsons (glisser-déposer)
- [ ] Système de notifications en temps réel
- [ ] Export CSV des résultats pour les professeurs
- [ ] Mode sombre
- [ ] Support mobile amélioré
- [ ] Tests unitaires automatisés
- [ ] Documentation API REST (si nécessaire)

---

## 📧 Support

Pour toute question ou problème, contactez l'équipe de développement.

**Bon apprentissage ! 🎓💻**
