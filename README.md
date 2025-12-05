# Portail d'apprentissage NSI

Application web éducative pour l'enseignement de la NSI (Numérique et Sciences Informatiques) au lycée.

## Stack technique

- **Backend**: Django 5
- **Base de données**: PostgreSQL
- **Frontend**: Django templates + HTMX + Tailwind CSS
- **Éditeur de code**: Monaco Editor
- **Exécution Python**: Pyodide (WebAssembly)
- **Exécution SQL**: sql.js (SQLite en mémoire)

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer les variables d'environnement :
```bash
copy .env.example .env
# Éditer .env avec vos paramètres
```

4. Créer la base de données PostgreSQL :
```sql
CREATE DATABASE nsi_platform;
```

5. Appliquer les migrations :
```bash
python manage.py migrate
```

6. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

7. Charger les données initiales (optionnel) :
```bash
python manage.py loaddata fixtures/initial_data.json
```

8. Lancer le serveur :
```bash
python manage.py runserver
```

## Structure du projet

```
NSI_portal/
├── accounts/          # Gestion utilisateurs, classes
├── courses/           # Cours et chapitres
├── exercises/         # Exercices et tentatives
├── gamification/      # Badges, XP, achievements
├── nsi_project/       # Configuration Django
├── templates/         # Templates globaux
└── static/           # CSS, JS, images
```

## Fonctionnalités

### Pour les élèves
- Inscription avec pseudo et code de classe
- Suivi de progression par chapitre
- Exercices interactifs (Python, SQL, QCM)
- Système de XP et badges
- Historique des tentatives

### Pour les professeurs
- Création et gestion de classes
- Attribution de chapitres
- Suivi de la progression des élèves
- Statistiques de classe

### Pour les admins
- Gestion des cours et chapitres
- Création d'exercices
- Configuration des badges

## Licence

Ce projet est sous licence MIT.
