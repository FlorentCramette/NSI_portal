"""
Content data for Seconde NSI courses
Separated for better maintainability
"""

# Python course chapters content
PYTHON_CHAPTERS = [
    {
        'slug': 'introduction-python',
        'title': 'Introduction à Python',
        'description': 'Premiers pas avec Python',
        'order': 1,
        'content_blocks': [
            {
                'type': 'TEXT',
                'title': 'Qu\'est-ce que Python ?',
                'order': 1,
                'content_markdown': '''# Bienvenue en Python ! 🐍

Python est un langage de programmation **simple** et **puissant** utilisé par des millions de développeurs dans le monde.

## Pourquoi Python ?

- ✅ **Facile à apprendre** : syntaxe claire et lisible
- ✅ **Polyvalent** : sites web, jeux, intelligence artificielle...
- ✅ **Très populaire** : grandes entreprises (Google, NASA, Netflix)

## Votre premier programme

```python
print("Bonjour le monde !")
```

Cette simple ligne affiche un message à l'écran. C'est votre premier programme Python ! 🎉
'''
            }
        ],
        'exercises': [
            {
                'title': 'Afficher un message',
                'type': 'PYTHON',
                'order': 1,
                'xp_reward': 10,
                'statement_markdown': '''Écrivez un programme qui affiche "Bienvenue en NSI !"

**Aide :** Utilisez la fonction `print()` pour afficher du texte.
''',
                'starter_code': '# Écrivez votre code ici\n',
                'tests_definition': {
                    'tests': [
                        {
                            'name': 'Affichage correct',
                            'code': 'print("Bienvenue en NSI !")',
                            'expected_output': 'Bienvenue en NSI !'
                        }
                    ]
                }
            }
        ]
    },
    {
        'slug': 'variables-et-types',
        'title': 'Variables et Types de Données',
        'description': 'Stocker des informations dans des variables',
        'order': 2,
        'content_blocks': [
            {
                'type': 'TEXT',
                'title': 'Les variables',
                'order': 1,
                'content_markdown': '''# Les Variables 📦

Une **variable** est comme une boîte qui stocke une valeur.

## Types de données principaux

```python
# Nombres entiers (int)
age = 15
nombre_eleves = 30

# Nombres décimaux (float)
note = 15.5
pi = 3.14159

# Texte (str)
prenom = "Alice"
message = "Bonjour !"

# Booléens (bool)
est_majeur = False
a_reussi = True
```

## Règles de nommage

✅ Bon :
- `mon_age`, `nombre_1`, `prenom_eleve`

❌ Mauvais :
- `1nombre` (ne commence pas par un chiffre)
- `mon-age` (pas de tirets)
- `class` (mot réservé)
'''
            }
        ],
        'exercises': [
            {
                'title': 'Créer et calculer',
                'type': 'PYTHON',
                'order': 1,
                'xp_reward': 15,
                'statement_markdown': '''Créez une fonction `calculer_somme(a, b)` qui retourne la somme de deux nombres.

**Exemples :**
```python
calculer_somme(5, 3)  # Doit retourner 8
calculer_somme(10, 20)  # Doit retourner 30
```
''',
                'starter_code': '''def calculer_somme(a, b):
    # Complétez cette fonction
    pass
''',
                'tests_definition': {
                    'tests': [
                        {'name': 'Somme de 5 et 3', 'code': 'calculer_somme(5, 3)', 'expected': 8},
                        {'name': 'Somme de 10 et 20', 'code': 'calculer_somme(10, 20)', 'expected': 30},
                        {'name': 'Somme avec zéro', 'code': 'calculer_somme(0, 15)', 'expected': 15}
                    ]
                }
            }
        ]
    }
]

# Add more chapters as needed...
