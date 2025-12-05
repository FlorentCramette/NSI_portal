# 📚 Bibliothèque d'Exercices - NSI Portal

Ce document contient des exemples d'exercices prêts à l'emploi pour différents niveaux et thèmes du programme NSI.

---

## 🐍 Exercices Python

### 1. Les bases - Variables et types

#### Exercice : Calculatrice simple
```json
{
  "title": "Calculatrice de base",
  "type": "PYTHON",
  "statement_markdown": "Créez une fonction `calculer(a, b, operation)` qui effectue l'opération spécifiée (+, -, *, /) sur deux nombres.\n\n**Exemple :**\n```python\ncalculer(10, 5, '+')  # Doit retourner 15\ncalculer(10, 5, '*')  # Doit retourner 50\n```",
  "starter_code": "def calculer(a, b, operation):\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Addition",
        "code": "calculer(10, 5, '+')",
        "expected": 15
      },
      {
        "name": "Soustraction",
        "code": "calculer(10, 5, '-')",
        "expected": 5
      },
      {
        "name": "Multiplication",
        "code": "calculer(10, 5, '*')",
        "expected": 50
      },
      {
        "name": "Division",
        "code": "calculer(10, 5, '/')",
        "expected": 2.0
      }
    ]
  },
  "xp_reward": 15
}
```

---

### 2. Les listes

#### Exercice : Trouver le maximum
```json
{
  "title": "Maximum d'une liste",
  "type": "PYTHON",
  "statement_markdown": "Écrivez une fonction `trouver_max(liste)` qui retourne le plus grand élément d'une liste de nombres **sans utiliser la fonction max()**.\n\n**Exemple :**\n```python\ntrouver_max([3, 7, 2, 9, 1])  # Doit retourner 9\n```",
  "starter_code": "def trouver_max(liste):\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Liste simple",
        "code": "trouver_max([3, 7, 2, 9, 1])",
        "expected": 9
      },
      {
        "name": "Nombres négatifs",
        "code": "trouver_max([-5, -2, -8, -1])",
        "expected": -1
      },
      {
        "name": "Un seul élément",
        "code": "trouver_max([42])",
        "expected": 42
      }
    ]
  },
  "xp_reward": 20
}
```

#### Exercice : Filtrer les pairs
```json
{
  "title": "Nombres pairs",
  "type": "PYTHON",
  "statement_markdown": "Créez une fonction `nombres_pairs(liste)` qui retourne une nouvelle liste contenant uniquement les nombres pairs.\n\n**Exemple :**\n```python\nnombres_pairs([1, 2, 3, 4, 5, 6])  # Doit retourner [2, 4, 6]\n```",
  "starter_code": "def nombres_pairs(liste):\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Liste mixte",
        "code": "nombres_pairs([1, 2, 3, 4, 5, 6])",
        "expected": [2, 4, 6]
      },
      {
        "name": "Aucun pair",
        "code": "nombres_pairs([1, 3, 5, 7])",
        "expected": []
      },
      {
        "name": "Tous pairs",
        "code": "nombres_pairs([2, 4, 6, 8])",
        "expected": [2, 4, 6, 8]
      }
    ]
  },
  "xp_reward": 15
}
```

---

### 3. Les dictionnaires

#### Exercice : Compter les occurrences
```json
{
  "title": "Fréquence des caractères",
  "type": "PYTHON",
  "statement_markdown": "Écrivez une fonction `compter_caracteres(texte)` qui retourne un dictionnaire avec la fréquence de chaque caractère.\n\n**Exemple :**\n```python\ncompter_caracteres('hello')  # Doit retourner {'h': 1, 'e': 1, 'l': 2, 'o': 1}\n```",
  "starter_code": "def compter_caracteres(texte):\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Mot simple",
        "code": "compter_caracteres('hello')",
        "expected": {"h": 1, "e": 1, "l": 2, "o": 1}
      },
      {
        "name": "Lettres répétées",
        "code": "compter_caracteres('aaa')",
        "expected": {"a": 3}
      },
      {
        "name": "Chaîne vide",
        "code": "compter_caracteres('')",
        "expected": {}
      }
    ]
  },
  "xp_reward": 25
}
```

---

### 4. Algorithmes de tri

#### Exercice : Tri à bulles
```json
{
  "title": "Tri à bulles",
  "type": "PYTHON",
  "statement_markdown": "Implémentez l'algorithme de **tri à bulles** dans une fonction `tri_bulles(liste)` qui trie une liste de nombres par ordre croissant.\n\n**Principe :**\n- Comparer chaque paire d'éléments adjacents\n- Les échanger s'ils sont dans le mauvais ordre\n- Répéter jusqu'à ce que la liste soit triée\n\n**Exemple :**\n```python\ntri_bulles([64, 34, 25, 12, 22])  # Doit retourner [12, 22, 25, 34, 64]\n```",
  "starter_code": "def tri_bulles(liste):\n    # À compléter\n    n = len(liste)\n    # Votre code ici\n    return liste",
  "tests_definition": {
    "tests": [
      {
        "name": "Liste non triée",
        "code": "tri_bulles([64, 34, 25, 12, 22])",
        "expected": [12, 22, 25, 34, 64]
      },
      {
        "name": "Liste déjà triée",
        "code": "tri_bulles([1, 2, 3, 4, 5])",
        "expected": [1, 2, 3, 4, 5]
      },
      {
        "name": "Nombres négatifs",
        "code": "tri_bulles([3, -1, 4, -5, 2])",
        "expected": [-5, -1, 2, 3, 4]
      }
    ]
  },
  "xp_reward": 30
}
```

---

### 5. Récursivité

#### Exercice : Factorielle
```json
{
  "title": "Factorielle récursive",
  "type": "PYTHON",
  "statement_markdown": "Écrivez une fonction **récursive** `factorielle(n)` qui calcule la factorielle d'un nombre.\n\n**Rappel :** n! = n × (n-1) × (n-2) × ... × 1\n\n**Exemple :**\n```python\nfactorielle(5)  # Doit retourner 120 (5 × 4 × 3 × 2 × 1)\n```",
  "starter_code": "def factorielle(n):\n    # Cas de base\n    if n == 0:\n        return 1\n    # Cas récursif\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Factorielle de 0",
        "code": "factorielle(0)",
        "expected": 1
      },
      {
        "name": "Factorielle de 1",
        "code": "factorielle(1)",
        "expected": 1
      },
      {
        "name": "Factorielle de 5",
        "code": "factorielle(5)",
        "expected": 120
      },
      {
        "name": "Factorielle de 10",
        "code": "factorielle(10)",
        "expected": 3628800
      }
    ]
  },
  "xp_reward": 25
}
```

#### Exercice : Suite de Fibonacci
```json
{
  "title": "Fibonacci récursif",
  "type": "PYTHON",
  "statement_markdown": "Implémentez la suite de Fibonacci de manière **récursive** : `fibonacci(n)`.\n\n**Rappel :** \n- fibonacci(0) = 0\n- fibonacci(1) = 1\n- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)\n\n**Exemple :**\n```python\nfibonacci(6)  # Doit retourner 8 (0, 1, 1, 2, 3, 5, 8)\n```",
  "starter_code": "def fibonacci(n):\n    # À compléter\n    pass",
  "tests_definition": {
    "tests": [
      {
        "name": "Fibo(0)",
        "code": "fibonacci(0)",
        "expected": 0
      },
      {
        "name": "Fibo(1)",
        "code": "fibonacci(1)",
        "expected": 1
      },
      {
        "name": "Fibo(6)",
        "code": "fibonacci(6)",
        "expected": 8
      },
      {
        "name": "Fibo(10)",
        "code": "fibonacci(10)",
        "expected": 55
      }
    ]
  },
  "xp_reward": 30
}
```

---

## 🗄️ Exercices SQL

### 1. Requêtes SELECT simples

#### Exercice : Sélection de base
```json
{
  "title": "SELECT basique",
  "type": "SQL",
  "statement_markdown": "Écrivez une requête SQL qui sélectionne **tous les élèves** de la table `eleves`.\n\nLa table contient les colonnes : `id`, `nom`, `prenom`, `age`.",
  "starter_code": "-- Écrivez votre requête SQL ici\n",
  "tests_definition": {
    "schema": "CREATE TABLE eleves (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER);",
    "data": "INSERT INTO eleves VALUES (1, 'Dupont', 'Alice', 16), (2, 'Martin', 'Bob', 17), (3, 'Durand', 'Charlie', 16);",
    "tests": [
      {
        "name": "Sélectionner tous les élèves",
        "solution": "SELECT * FROM eleves ORDER BY id",
        "expected_columns": ["id", "nom", "prenom", "age"],
        "expected_rows": [
          [1, "Dupont", "Alice", 16],
          [2, "Martin", "Bob", 17],
          [3, "Durand", "Charlie", 16]
        ]
      }
    ]
  },
  "xp_reward": 10
}
```

---

### 2. Filtrage avec WHERE

#### Exercice : Filtrer par âge
```json
{
  "title": "Clause WHERE",
  "type": "SQL",
  "statement_markdown": "Sélectionnez tous les élèves qui ont **16 ans ou plus**.\n\nAffichez les colonnes `nom`, `prenom` et `age`, triés par nom.",
  "starter_code": "-- Écrivez votre requête SQL ici\n",
  "tests_definition": {
    "schema": "CREATE TABLE eleves (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER);",
    "data": "INSERT INTO eleves VALUES (1, 'Dupont', 'Alice', 15), (2, 'Martin', 'Bob', 17), (3, 'Durand', 'Charlie', 16);",
    "tests": [
      {
        "name": "Élèves de 16 ans ou plus",
        "solution": "SELECT nom, prenom, age FROM eleves WHERE age >= 16 ORDER BY nom",
        "expected_columns": ["nom", "prenom", "age"],
        "expected_rows": [
          ["Durand", "Charlie", 16],
          ["Martin", "Bob", 17]
        ]
      }
    ]
  },
  "xp_reward": 15
}
```

---

### 3. Agrégation

#### Exercice : Compter et moyenner
```json
{
  "title": "Fonctions d'agrégation",
  "type": "SQL",
  "statement_markdown": "Calculez :\n1. Le **nombre total** d'élèves\n2. L'**âge moyen** des élèves\n\nUtilisez les fonctions `COUNT()` et `AVG()`.\n\nVotre requête doit retourner deux colonnes : `total` et `age_moyen`.",
  "starter_code": "-- Écrivez votre requête SQL ici\n",
  "tests_definition": {
    "schema": "CREATE TABLE eleves (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, age INTEGER);",
    "data": "INSERT INTO eleves VALUES (1, 'Dupont', 'Alice', 16), (2, 'Martin', 'Bob', 17), (3, 'Durand', 'Charlie', 16);",
    "tests": [
      {
        "name": "Compter et moyenner",
        "solution": "SELECT COUNT(*) as total, AVG(age) as age_moyen FROM eleves",
        "expected_columns": ["total", "age_moyen"],
        "expected_rows": [
          [3, 16.333333333333332]
        ]
      }
    ]
  },
  "xp_reward": 20
}
```

---

### 4. Jointures

#### Exercice : JOIN simple
```json
{
  "title": "Jointure entre tables",
  "type": "SQL",
  "statement_markdown": "Vous avez deux tables :\n- `eleves` (id, nom, classe_id)\n- `classes` (id, nom_classe)\n\nÉcrivez une requête qui affiche le **nom de l'élève** et le **nom de sa classe**.\n\nAffichez les colonnes `nom` et `nom_classe`, triés par nom d'élève.",
  "starter_code": "-- Écrivez votre requête SQL ici\n",
  "tests_definition": {
    "schema": "CREATE TABLE classes (id INTEGER PRIMARY KEY, nom_classe TEXT); CREATE TABLE eleves (id INTEGER PRIMARY KEY, nom TEXT, classe_id INTEGER);",
    "data": "INSERT INTO classes VALUES (1, 'Terminale NSI'), (2, 'Première NSI'); INSERT INTO eleves VALUES (1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1);",
    "tests": [
      {
        "name": "Jointure élèves-classes",
        "solution": "SELECT eleves.nom, classes.nom_classe FROM eleves JOIN classes ON eleves.classe_id = classes.id ORDER BY eleves.nom",
        "expected_columns": ["nom", "nom_classe"],
        "expected_rows": [
          ["Alice", "Terminale NSI"],
          ["Bob", "Première NSI"],
          ["Charlie", "Terminale NSI"]
        ]
      }
    ]
  },
  "xp_reward": 30
}
```

---

## 🧩 Exercices Parsons (QCM de tri de lignes)

### Exercice : Trier les lignes de code

```json
{
  "title": "Tri par insertion - Ordonner le code",
  "type": "PARSONS",
  "statement_markdown": "Remettez les lignes de code dans le bon ordre pour implémenter un **tri par insertion**.",
  "tests_definition": {
    "lines": [
      "def tri_insertion(liste):",
      "    for i in range(1, len(liste)):",
      "        cle = liste[i]",
      "        j = i - 1",
      "        while j >= 0 and liste[j] > cle:",
      "            liste[j + 1] = liste[j]",
      "            j -= 1",
      "        liste[j + 1] = cle",
      "    return liste"
    ],
    "correct_order": [0, 1, 2, 3, 4, 5, 6, 7, 8]
  },
  "xp_reward": 20
}
```

---

## 📝 Conseils pour créer des exercices

### Bonnes pratiques

1. **Progressivité** : Commencez simple, augmentez la difficulté graduellement
2. **Tests variés** : Cas normaux, cas limites, cas d'erreur
3. **XP proportionnelle** : 10-15 XP (facile), 20-25 XP (moyen), 30+ XP (difficile)
4. **Instructions claires** : Exemples concrets, format attendu
5. **Starter code** : Aidez les élèves à démarrer avec une structure

### Structure d'un bon exercice

```markdown
1. **Contexte** : Pourquoi cet exercice est utile
2. **Objectif** : Ce que l'élève doit accomplir
3. **Exemples** : 2-3 exemples d'utilisation
4. **Contraintes** : Interdire certaines fonctions si nécessaire
5. **Indices** : Hints progressifs (avec coût XP)
```

### Idées de thèmes avancés

- 🌳 **Structures de données** : Piles, files, arbres, graphes
- 🔍 **Algorithmes de recherche** : Recherche binaire, parcours
- 🔐 **Cryptographie** : Chiffrement César, substitution
- 🎲 **Jeux** : Puissance 4, Morpion, Sudoku
- 📊 **Traitement de données** : CSV, JSON, statistiques
- 🌐 **Web scraping** : Parser HTML, extraire données
- 🤖 **Intelligence artificielle** : MinMax, A*, réseaux neuronaux simples

---

**Bonne création d'exercices ! 🎓**
