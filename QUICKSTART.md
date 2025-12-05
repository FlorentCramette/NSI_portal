# 🚀 Guide de Démarrage Rapide - NSI Portal

## Installation en 5 minutes

### 1. Cloner et configurer l'environnement

```powershell
# Se placer dans le répertoire du projet
cd C:\dev\NSI_portal

# Créer un environnement virtuel Python
python -m venv venv

# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configurer la base de données PostgreSQL

**Option A : PostgreSQL local**
```powershell
# Dans pgAdmin ou psql, créer la base de données
CREATE DATABASE nsi_platform;
CREATE USER nsi_user WITH PASSWORD 'nsi_password123';
ALTER ROLE nsi_user SET client_encoding TO 'utf8';
ALTER ROLE nsi_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE nsi_user SET timezone TO 'Europe/Paris';
GRANT ALL PRIVILEGES ON DATABASE nsi_platform TO nsi_user;
```

**Option B : SQLite (développement uniquement)**
Modifier dans `nsi_project/settings.py` :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 3. Configuration des variables d'environnement

Créer un fichier `.env` à la racine :
```ini
SECRET_KEY=votre-clé-secrète-très-longue-et-aléatoire
DEBUG=True

# PostgreSQL
DB_NAME=nsi_platform
DB_USER=nsi_user
DB_PASSWORD=nsi_password123
DB_HOST=localhost
DB_PORT=5432
```

### 4. Initialiser la base de données

```powershell
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer des données de test
python manage.py create_sample_data
```

### 5. Lancer le serveur

```powershell
python manage.py runserver
```

Ouvrez votre navigateur sur : **http://127.0.0.1:8000**

---

## 📝 Comptes de test créés

Après avoir exécuté `create_sample_data`, vous pouvez vous connecter avec :

### 👨‍💼 Administrateur
- **Identifiant** : `admin`
- **Mot de passe** : `admin123`
- **Accès** : Interface d'administration Django + toutes les fonctionnalités

### 👨‍🏫 Professeur
- **Identifiant** : `prof_martin`
- **Mot de passe** : `prof123`
- **Accès** : Création de classes, gestion d'élèves, suivi des progrès

### 👨‍🎓 Élève
- **Identifiant** : `eleve_alice`
- **Mot de passe** : `eleve123`
- **Accès** : Cours, exercices, badges, classement

---

## 🎯 Premiers pas

### Pour les professeurs

1. **Connexion** : Connectez-vous avec `prof_martin / prof123`

2. **Créer une classe** :
   - Allez dans "Mes Classes" → "Créer une classe"
   - Entrez le nom et l'établissement
   - Notez le **code de classe** généré (ex: `ABC123`)

3. **Partager le code** avec vos élèves

4. **Assigner des chapitres** :
   - Ouvrez votre classe
   - Cliquez sur "Assigner un chapitre"
   - Sélectionnez un cours et un chapitre

5. **Suivre la progression** :
   - Tableau de bord avec statistiques globales
   - Liste des élèves avec leur progression individuelle

### Pour les élèves

1. **Connexion** : Connectez-vous avec `eleve_alice / eleve123`

2. **Rejoindre une classe** :
   - Allez dans "Rejoindre une classe"
   - Entrez le code fourni par votre professeur
   - Validez

3. **Commencer un cours** :
   - Parcourez les cours disponibles
   - Cliquez sur "Continuer" ou "Voir le cours"
   - Lisez les chapitres et faites les exercices

4. **Faire un exercice** :
   - Cliquez sur un exercice
   - Écrivez votre code dans l'éditeur
   - Testez avec le bouton "Tester"
   - Soumettez avec "Valider"

5. **Gagner des XP et badges** :
   - Réussissez des exercices pour gagner de l'XP
   - Montez de niveau automatiquement
   - Débloquez des badges en atteignant des objectifs
   - Comparez-vous aux autres dans le classement

---

## 📚 Créer du contenu

### Ajouter un cours (via l'admin Django)

1. Accédez à http://127.0.0.1:8000/admin
2. Connectez-vous avec `admin / admin123`
3. Allez dans **Courses** → **Courses** → **Add course**
4. Remplissez :
   - Title : "Structures de données"
   - Level : Première ou Terminale
   - Description : Description du cours
   - Icon : 📊 (emoji de votre choix)
   - Order : 1, 2, 3...
   - Is published : ✓

### Ajouter un chapitre

1. Dans l'admin : **Courses** → **Chapters** → **Add chapter**
2. Remplissez :
   - Course : Sélectionnez le cours
   - Title : "Les listes en Python"
   - Slug : `listes-python` (auto-généré)
   - Description : Description du chapitre
   - Order : 1, 2, 3...
   - Is published : ✓

### Ajouter un exercice Python

1. Dans l'admin : **Exercises** → **Exercises** → **Add exercise**
2. Remplissez :
   - Chapter : Sélectionnez le chapitre
   - Title : "Inverser une liste"
   - Type : Python
   - Statement markdown :
     ```markdown
     Écrivez une fonction `inverser(liste)` qui retourne une nouvelle liste avec les éléments inversés.
     
     **Exemple :**
     ```python
     inverser([1, 2, 3])  # Doit retourner [3, 2, 1]
     ```
     ```
   - Starter code :
     ```python
     def inverser(liste):
         # À compléter
         pass
     ```
   - Tests definition (JSON) :
     ```json
     {
       "tests": [
         {
           "name": "Test 1 : Liste simple",
           "code": "inverser([1, 2, 3])",
           "expected": [3, 2, 1]
         },
         {
           "name": "Test 2 : Liste vide",
           "code": "inverser([])",
           "expected": []
         },
         {
           "name": "Test 3 : Un élément",
           "code": "inverser([42])",
           "expected": [42]
         }
       ]
     }
     ```
   - XP reward : 15
   - Order : 1, 2, 3...
   - Is published : ✓

### Ajouter un exercice SQL

1. Dans l'admin : **Exercises** → **Exercises** → **Add exercise**
2. Type : SQL
3. Tests definition (JSON) :
   ```json
   {
     "schema": "CREATE TABLE eleves (id INTEGER PRIMARY KEY, nom TEXT, age INTEGER);",
     "data": "INSERT INTO eleves VALUES (1, 'Alice', 16), (2, 'Bob', 17);",
     "tests": [
       {
         "name": "Sélectionner tous les élèves",
         "solution": "SELECT * FROM eleves ORDER BY id",
         "expected_columns": ["id", "nom", "age"],
         "expected_rows": [
           [1, "Alice", 16],
           [2, "Bob", 17]
         ]
       }
     ]
   }
   ```

---

## 🎮 Système de gamification

### Badges automatiques

Les badges se débloquent automatiquement selon l'XP :
- 🌱 **Débutant** : 0 XP
- 🥉 **Bronze** : 100 XP
- 🥈 **Argent** : 500 XP
- 🥇 **Or** : 1000 XP

### Succès (Achievements)

Des succès se débloquent pour des actions spécifiques :
- 🎯 **Premier pas** : Réussir le premier exercice (+50 XP)
- 🔟 **Persévérant** : Réussir 10 exercices (+100 XP)

Vous pouvez en ajouter dans `gamification/utils.py`.

---

## 🛠️ Commandes utiles

```powershell
# Créer un superuser manuellement
python manage.py createsuperuser

# Réinitialiser la base de données (ATTENTION : efface tout)
python manage.py flush
python manage.py migrate
python manage.py create_sample_data

# Collecter les fichiers statiques (production)
python manage.py collectstatic

# Lancer les tests
python manage.py test

# Shell Django pour tester du code
python manage.py shell
```

---

## 📊 Statistiques disponibles

### Pour les professeurs

Dans le dashboard et les détails de classe :
- Nombre total d'élèves
- Nombre de tentatives d'exercices
- Taux de réussite moyen
- XP moyen par élève
- Progression par élève
- Dernière activité de chaque élève

### Pour les élèves

Dans le dashboard et le profil :
- Niveau et XP actuels
- Progression vers le niveau suivant
- Nombre d'exercices réussis
- Taux de réussite personnel
- Badges et succès obtenus
- Classement dans la classe
- Historique des tentatives

---

## 🔧 Personnalisation

### Changer les couleurs (Tailwind)

Modifiez `templates/base.html` :
```html
<!-- Remplacer bg-blue-600 par bg-purple-600, etc. -->
```

### Ajouter un nouveau type d'exercice

1. Modifiez `exercises/models.py` → `ExerciseType`
2. Ajoutez la logique dans `static/js/code_execution.js`
3. Mettez à jour le template `exercise_detail.html`

### Ajouter une nouvelle statistique

1. Créez un custom template tag dans `accounts/templatetags/custom_tags.py`
2. Utilisez-le dans les templates avec `{% load custom_tags %}`

---

## ❓ Résolution de problèmes

### Erreur "No module named 'psycopg2'"
```powershell
pip install psycopg2-binary
```

### Erreur "FATAL: password authentication failed"
Vérifiez les credentials dans `.env` et PostgreSQL.

### Les migrations échouent
```powershell
python manage.py migrate --run-syncdb
```

### Le JavaScript ne fonctionne pas
Vérifiez la console du navigateur (F12) pour les erreurs.

### Les templates ne se chargent pas
Vérifiez que `DEBUG=True` dans `.env` et redémarrez le serveur.

---

## 📞 Support

Pour toute question :
1. Consultez la documentation complète dans `README.md` et `INSTALLATION.md`
2. Vérifiez les logs du serveur Django dans le terminal
3. Inspectez la console du navigateur pour les erreurs JavaScript

---

**Bon coding ! 🚀**
