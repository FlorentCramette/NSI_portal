from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI 1ère Programmation Python course'

    def handle(self, *args, **options):
        self.stdout.write('Creating NSI Programmation Python content...')
        
        try:
            course = Course.objects.get(slug='nsi-1-programmation')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course not found'))
            return
        
        course.chapters.all().delete()
        
        # Chapter 1: Types et variables
        chapter1 = Chapter.objects.create(
            course=course,
            title="Types de données et variables",
            description="Maîtriser les types de base en Python",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Les types de données",
            content_markdown="""## Types fondamentaux en Python

Python dispose de plusieurs types de données intégrés:

### Types numériques
- **int** : Entiers (ex: `42`, `-15`, `1000`)
- **float** : Nombres à virgule (ex: `3.14`, `-0.5`, `2.0`)
- **complex** : Nombres complexes (ex: `3+4j`)

### Types séquentiels
- **str** : Chaînes de caractères (ex: `"Bonjour"`, `'Python'`)
- **list** : Listes modifiables (ex: `[1, 2, 3]`)
- **tuple** : Tuples immuables (ex: `(1, 2, 3)`)

### Types de collections
- **dict** : Dictionnaires clé-valeur (ex: `{"nom": "Alice", "age": 17}`)
- **set** : Ensembles non ordonnés (ex: `{1, 2, 3}`)

### Type booléen
- **bool** : Vrai ou Faux (`True`, `False`)

## Variables

Une variable est un **nom** qui référence une **valeur** en mémoire.

### Règles de nommage
✅ **Autorisé:**
- Lettres (a-z, A-Z), chiffres (0-9), underscore (_)
- Commence par une lettre ou _
- Sensible à la casse: `age` ≠ `Age`

❌ **Interdit:**
- Mots-clés Python: `if`, `for`, `class`, etc.
- Espaces, caractères spéciaux (@, !, ?, etc.)
- Commence par un chiffre

### Conventions
- **snake_case** : `mon_age`, `nombre_eleves` (recommandé)
- **CamelCase** : `MonAge` (pour les classes)
- Variables en minuscules
- Constantes en MAJUSCULES: `PI = 3.14159`""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Pratique: Manipulation des types",
            content_markdown="""# Exemples de types de données

# Types numériques
entier = 42
reel = 3.14
print(f"Entier: {entier}, type: {type(entier)}")
print(f"Réel: {reel}, type: {type(reel)}")

# Chaînes de caractères
prenom = "Alice"
nom = 'Dupont'
print(f"Nom complet: {prenom} {nom}")

# Listes (modifiables)
nombres = [1, 2, 3, 4, 5]
nombres.append(6)
print(f"Liste: {nombres}")

# Tuples (immuables)
coordonnees = (48.8566, 2.3522)  # Paris
print(f"Coordonnées: {coordonnees}")

# Dictionnaires
personne = {
    "nom": "Dupont",
    "prenom": "Alice",
    "age": 17,
    "classe": "1ère NSI"
}
print(f"Personne: {personne['prenom']} {personne['nom']}")

# Booléens
est_majeur = False
a_le_bac = False
print(f"Majeur: {est_majeur}")

# Conversion de types (cast)
nombre_str = "42"
nombre_int = int(nombre_str)
print(f"'{nombre_str}' converti en int: {nombre_int}")

moyenne = 15.7
moyenne_str = str(moyenne)
print(f"{moyenne} converti en str: '{moyenne_str}'")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Types et variables",
            content_markdown="""**Question 1:** Quel est le type de la valeur `3.14` ?
- a) int
- b) float ✓
- c) str
- d) bool

**Question 2:** Quelle variable respecte les conventions Python ?
- a) 1variable
- b) ma-variable
- c) ma_variable ✓
- d) class

**Question 3:** Quelle structure est **immuable** ?
- a) list
- b) dict
- c) tuple ✓
- d) set

**Question 4:** Que fait `int("42")` ?
- a) Erreur
- b) Convertit la chaîne en entier ✓
- c) Retourne "42"
- d) Retourne 42.0""",
            order=3
        )
        
        # Chapter 2: Structures conditionnelles
        chapter2 = Chapter.objects.create(
            course=course,
            title="Structures conditionnelles",
            description="Prendre des décisions avec if, elif, else",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les instructions conditionnelles",
            content_markdown="""## Structure if / elif / else

Les conditions permettent d'exécuter du code **seulement si** une condition est vraie.

### Syntaxe de base

```python
if condition:
    # Code exécuté si condition est True
    instructions
```

**Important:** L'indentation (4 espaces) est **obligatoire** en Python!

### If / Else

```python
if condition:
    # Si True
    instructions_si_vrai
else:
    # Si False
    instructions_si_faux
```

### If / Elif / Else

Pour tester plusieurs conditions:

```python
if condition1:
    instructions1
elif condition2:
    instructions2
elif condition3:
    instructions3
else:
    instructions_par_defaut
```

## Opérateurs de comparaison

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `==` | Égal à | `x == 5` |
| `!=` | Différent de | `x != 0` |
| `<` | Inférieur à | `x < 10` |
| `>` | Supérieur à | `x > 0` |
| `<=` | Inférieur ou égal | `x <= 20` |
| `>=` | Supérieur ou égal | `x >= 18` |

## Opérateurs logiques

| Opérateur | Signification | Exemple |
|-----------|---------------|---------|
| `and` | ET logique | `x > 0 and x < 10` |
| `or` | OU logique | `x < 0 or x > 100` |
| `not` | NON logique | `not est_vide` |

### Tables de vérité

**AND (et):**
- `True and True` → `True`
- `True and False` → `False`
- `False and True` → `False`
- `False and False` → `False`

**OR (ou):**
- `True or True` → `True`
- `True or False` → `True`
- `False or True` → `True`
- `False or False` → `False`

**NOT (non):**
- `not True` → `False`
- `not False` → `True`""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Pratique: Conditions",
            content_markdown="""# Exemples de conditions

# Exemple 1: Majorité
age = 17
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

# Exemple 2: Mention au bac
moyenne = 15.5

if moyenne >= 16:
    print("Mention Très Bien")
elif moyenne >= 14:
    print("Mention Bien")
elif moyenne >= 12:
    print("Mention Assez Bien")
elif moyenne >= 10:
    print("Admis sans mention")
else:
    print("Non admis")

# Exemple 3: Opérateurs logiques
temperature = 25
pluie = False

if temperature > 20 and not pluie:
    print("Parfait pour une sortie!")
elif temperature > 20 and pluie:
    print("Il fait chaud mais il pleut")
elif temperature <= 20 and not pluie:
    print("Un peu frais mais pas de pluie")
else:
    print("Mauvais temps")

# Exemple 4: Vérification de mot de passe
mot_de_passe = "Python123"
longueur_ok = len(mot_de_passe) >= 8
a_chiffre = any(c.isdigit() for c in mot_de_passe)
a_lettre = any(c.isalpha() for c in mot_de_passe)

if longueur_ok and a_chiffre and a_lettre:
    print("✓ Mot de passe fort")
else:
    print("✗ Mot de passe faible")
    if not longueur_ok:
        print("  - Doit faire au moins 8 caractères")
    if not a_chiffre:
        print("  - Doit contenir au moins un chiffre")
    if not a_lettre:
        print("  - Doit contenir au moins une lettre")

# Exemple 5: Années bissextiles
annee = 2024

if annee % 400 == 0:
    print(f"{annee} est bissextile (divisible par 400)")
elif annee % 100 == 0:
    print(f"{annee} n'est pas bissextile (divisible par 100)")
elif annee % 4 == 0:
    print(f"{annee} est bissextile (divisible par 4)")
else:
    print(f"{annee} n'est pas bissextile")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Calculateur d'IMC",
            content_markdown="""Crée un programme qui calcule l'**Indice de Masse Corporelle** (IMC).

**Formule:** IMC = poids / (taille²)

**Interprétation:**
- IMC < 18.5 : Sous-poids
- 18.5 ≤ IMC < 25 : Poids normal
- 25 ≤ IMC < 30 : Surpoids
- IMC ≥ 30 : Obésité

**Exemple de code:**
```python
poids = 70  # kg
taille = 1.75  # m

# Ton code ici
imc = poids / (taille ** 2)

# Afficher l'IMC et l'interprétation
print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Sous-poids")
elif imc < 25:
    print("Poids normal")
elif imc < 30:
    print("Surpoids")
else:
    print("Obésité")
```

**Bonus:** Ajoute des conseils personnalisés selon le résultat!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz: Conditions",
            content_markdown="""**Question 1:** Que retourne `5 > 3 and 2 < 1` ?
- a) True
- b) False ✓
- c) Erreur
- d) None

**Question 2:** Quelle est la bonne syntaxe pour "sinon si" ?
- a) elseif
- b) else if
- c) elif ✓
- d) elsif

**Question 3:** Que fait l'opérateur `not` ?
- a) Compare deux valeurs
- b) Inverse un booléen ✓
- c) Vérifie l'égalité
- d) Addition

**Question 4:** Combien d'espaces pour l'indentation en Python ?
- a) 2
- b) 4 ✓
- c) 8
- d) Peu importe""",
            order=4
        )
        
        # Chapter 3: Boucles
        chapter3 = Chapter.objects.create(
            course=course,
            title="Boucles for et while",
            description="Répéter des actions avec les boucles",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les boucles en Python",
            content_markdown="""## Boucle for

La boucle `for` parcourt une séquence (liste, chaîne, range, etc.)

### Syntaxe avec range()

```python
for i in range(5):
    print(i)  # Affiche 0, 1, 2, 3, 4
```

**range(n)** : génère 0, 1, 2, ..., n-1

**range(debut, fin)** : de debut à fin-1

**range(debut, fin, pas)** : avec un pas personnalisé

### Parcourir une liste

```python
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)
```

### Parcourir avec index

```python
fruits = ["pomme", "banane", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Boucle while

La boucle `while` continue **tant que** la condition est vraie.

### Syntaxe

```python
while condition:
    instructions
    # Modifier la condition!
```

⚠️ **Attention aux boucles infinies!** Il faut que la condition devienne False.

### Exemple

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1  # Important!
```

## Contrôle de boucle

### break
Arrête la boucle immédiatement:

```python
for i in range(10):
    if i == 5:
        break  # Sort de la boucle
    print(i)  # Affiche 0, 1, 2, 3, 4
```

### continue
Passe à l'itération suivante:

```python
for i in range(5):
    if i == 2:
        continue  # Saute 2
    print(i)  # Affiche 0, 1, 3, 4
```

## Boucles imbriquées

On peut mettre une boucle dans une boucle:

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

Résultat:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Pratique: Boucles",
            content_markdown="""# Exemples de boucles

# Exemple 1: Table de multiplication
nombre = 7
print(f"Table de {nombre}:")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} × {i} = {resultat}")

# Exemple 2: Somme des nombres
total = 0
for i in range(1, 101):
    total += i
print(f"Somme de 1 à 100: {total}")

# Exemple 3: Compter les voyelles
texte = "Bonjour Python"
voyelles = "aeiouAEIOU"
compte = 0
for lettre in texte:
    if lettre in voyelles:
        compte += 1
print(f"Nombre de voyelles: {compte}")

# Exemple 4: While avec saisie
tentatives = 0
max_tentatives = 3
mot_de_passe_correct = "python123"

while tentatives < max_tentatives:
    mdp = input("Mot de passe: ")
    if mdp == mot_de_passe_correct:
        print("✓ Accès autorisé!")
        break
    else:
        tentatives += 1
        restantes = max_tentatives - tentatives
        print(f"✗ Incorrect. {restantes} tentatives restantes")

if tentatives == max_tentatives:
    print("Compte bloqué!")

# Exemple 5: Motif avec boucles imbriquées
print("Triangle:")
for i in range(1, 6):
    print("*" * i)

print("\nCarré:")
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()  # Saut de ligne

# Exemple 6: Trouver les nombres premiers
print("\nNombres premiers jusqu'à 50:")
for nombre in range(2, 51):
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre, end=" ")
print()

# Exemple 7: Suite de Fibonacci
print("\nSuite de Fibonacci (10 premiers termes):")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Exercice: Jeu du nombre mystère",
            content_markdown="""Crée un jeu où l'ordinateur choisit un nombre entre 1 et 100, et le joueur doit le deviner.

**Fonctionnalités:**
1. Génère un nombre aléatoire avec `import random` et `random.randint(1, 100)`
2. Demande au joueur de deviner
3. Indique si le nombre est plus grand ou plus petit
4. Compte le nombre de tentatives
5. Félicite le joueur quand il trouve

**Structure:**
```python
import random

nombre_mystere = random.randint(1, 100)
tentatives = 0
trouve = False

print("=== JEU DU NOMBRE MYSTÈRE ===")
print("J'ai choisi un nombre entre 1 et 100")

while not trouve:
    # Ton code ici
    tentatives += 1
    proposition = int(input("Votre proposition: "))
    
    if proposition < nombre_mystere:
        print("↑ Plus grand!")
    elif proposition > nombre_mystere:
        print("↓ Plus petit!")
    else:
        print(f"🎉 Bravo! Trouvé en {tentatives} tentatives!")
        trouve = True
```

**Bonus:** Limite le nombre de tentatives à 7!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Boucles",
            content_markdown="""**Question 1:** Combien de fois cette boucle s'exécute: `for i in range(10)` ?
- a) 9 fois
- b) 10 fois ✓
- c) 11 fois
- d) Infiniment

**Question 2:** Que fait `break` dans une boucle ?
- a) Passe à l'itération suivante
- b) Sort de la boucle ✓
- c) Redémarre la boucle
- d) Provoque une erreur

**Question 3:** Quelle boucle utiliser pour un nombre d'itérations **inconnu** ?
- a) for
- b) while ✓
- c) if
- d) def

**Question 4:** Que génère `range(2, 8, 2)` ?
- a) 2, 3, 4, 5, 6, 7
- b) 2, 4, 6 ✓
- c) 2, 4, 6, 8
- d) 0, 2, 4, 6""",
            order=4
        )
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ Created {course.chapters.count()} chapters with '
            f'{ContentBlock.objects.filter(chapter__course=course).count()} blocks'
        ))
