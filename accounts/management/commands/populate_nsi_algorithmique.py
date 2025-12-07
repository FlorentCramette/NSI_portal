from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI 1ère Algorithmique course'

    def handle(self, *args, **options):
        self.stdout.write('Creating NSI Algorithmique content...')
        
        try:
            course = Course.objects.get(slug='nsi-1-algorithmique')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course not found'))
            return
        
        course.chapters.all().delete()
        
        # Chapter 1: Complexité algorithmique
        chapter1 = Chapter.objects.create(
            course=course,
            title="Complexité et efficacité des algorithmes",
            description="Mesurer et optimiser les performances",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Qu'est-ce que la complexité?",
            content_markdown="""## La complexité algorithmique

La **complexité** mesure les **ressources** utilisées par un algorithme:
- **Temps** : nombre d'opérations
- **Espace** : mémoire utilisée

### Pourquoi c'est important?

Deux algorithmes peuvent résoudre le même problème avec des performances **très différentes**!

**Exemple:** Chercher un nombre dans une liste

| Taille | Recherche linéaire | Recherche dichotomique |
|--------|-------------------|----------------------|
| 100 | 100 opérations | 7 opérations |
| 1 000 | 1 000 | 10 |
| 1 000 000 | 1 000 000 | 20 |
| 1 000 000 000 | 1 000 000 000 | 30 |

## Notation Big O

La notation **O(...)** décrit comment le temps d'exécution croît avec la taille des données.

### Complexités courantes

| Notation | Nom | Exemple | Description |
|----------|-----|---------|-------------|
| **O(1)** | Constante | Accès tableau | Toujours le même temps |
| **O(log n)** | Logarithmique | Recherche dichotomique | Double la taille → +1 opération |
| **O(n)** | Linéaire | Parcours liste | Double la taille → double le temps |
| **O(n log n)** | Quasi-linéaire | Tri fusion | Tri efficace |
| **O(n²)** | Quadratique | Tri à bulles | Double la taille → x4 temps |
| **O(2ⁿ)** | Exponentielle | Tours de Hanoï | TRÈS lent! |

### Visualisation

Pour n = 100:
- O(1) : **1** opération 🚀
- O(log n) : **7** opérations ⚡
- O(n) : **100** opérations ✅
- O(n log n) : **700** opérations 👍
- O(n²) : **10 000** opérations 🐌
- O(2ⁿ) : **1 267 650 600 228 229 401 496 703 205 376** opérations 💀

## Règles de calcul

### Règle 1: Ignorer les constantes
- O(2n) = O(n)
- O(n/2) = O(n)
- O(3n + 5) = O(n)

### Règle 2: Garder le terme dominant
- O(n² + n) = O(n²)
- O(n + log n) = O(n)
- O(n³ + n² + n) = O(n³)

### Règle 3: Boucles imbriquées
```python
for i in range(n):      # O(n)
    for j in range(n):  # O(n)
        print(i, j)     # O(1)
# Total: O(n × n) = O(n²)
```""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Pratique: Mesurer la complexité",
            content_markdown="""import time

# Fonction pour mesurer le temps d'exécution
def mesurer_temps(fonction, *args):
    debut = time.time()
    resultat = fonction(*args)
    fin = time.time()
    duree = (fin - debut) * 1000  # en millisecondes
    return resultat, duree

# O(1) - Complexité constante
def acces_direct(liste, index):
    return liste[index]

# O(n) - Complexité linéaire
def recherche_lineaire(liste, valeur):
    for element in liste:
        if element == valeur:
            return True
    return False

# O(log n) - Complexité logarithmique
def recherche_dichotomique(liste_triee, valeur):
    gauche, droite = 0, len(liste_triee) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste_triee[milieu] == valeur:
            return True
        elif liste_triee[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return False

# O(n²) - Complexité quadratique
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Tests comparatifs
print("=== COMPARAISON DE COMPLEXITÉS ===\n")

# Créer des listes de différentes tailles
tailles = [100, 1000, 10000]

for taille in tailles:
    liste = list(range(taille))
    
    # O(1) - Accès direct
    _, temps = mesurer_temps(acces_direct, liste, taille // 2)
    print(f"n={taille:5} | O(1) accès:     {temps:.4f} ms")
    
    # O(log n) - Recherche dichotomique
    _, temps = mesurer_temps(recherche_dichotomique, liste, taille - 1)
    print(f"n={taille:5} | O(log n) dicho: {temps:.4f} ms")
    
    # O(n) - Recherche linéaire
    _, temps = mesurer_temps(recherche_lineaire, liste, taille - 1)
    print(f"n={taille:5} | O(n) linéaire:  {temps:.4f} ms")
    
    print()

# Comparaison tri (petites listes)
print("=== TRI ===")
for taille in [10, 50, 100]:
    liste = list(range(taille, 0, -1))  # Liste inversée
    
    # O(n²) - Tri à bulles
    copie = liste.copy()
    _, temps = mesurer_temps(tri_bulles, copie)
    print(f"n={taille:3} | O(n²) bulles: {temps:.4f} ms")
    
    # O(n log n) - Tri Python (Timsort)
    copie = liste.copy()
    _, temps = mesurer_temps(sorted, copie)
    print(f"n={taille:3} | O(n log n):   {temps:.4f} ms")
    print()""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Complexité",
            content_markdown="""**Question 1:** Quelle est la complexité d'accéder à un élément dans une liste par son index?
- a) O(n)
- b) O(log n)
- c) O(1) ✓
- d) O(n²)

**Question 2:** Si un algorithme O(n) prend 1 seconde pour n=1000, combien de temps pour n=2000?
- a) 1 seconde
- b) 2 secondes ✓
- c) 4 secondes
- d) 1000 secondes

**Question 3:** Quelle complexité est la meilleure?
- a) O(n²)
- b) O(n log n)
- c) O(n)
- d) O(log n) ✓

**Question 4:** Deux boucles imbriquées de 1 à n donnent quelle complexité?
- a) O(n)
- b) O(2n)
- c) O(n²) ✓
- d) O(n log n)""",
            order=3
        )
        
        # Chapter 2: Algorithmes de tri
        chapter2 = Chapter.objects.create(
            course=course,
            title="Algorithmes de tri",
            description="Trier des données efficacement",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les algorithmes de tri",
            content_markdown="""## Pourquoi trier?

Le tri est une opération **fondamentale** en informatique:
- Facilite la recherche (recherche dichotomique)
- Organise les données
- Améliore la lisibilité
- Base de nombreux algorithmes

## Tri à bulles (Bubble Sort)

### Principe
Compare les éléments adjacents et les échange s'ils sont mal ordonnés.

### Algorithme
1. Parcourir la liste
2. Comparer chaque paire d'éléments adjacents
3. Échanger si ordre incorrect
4. Répéter jusqu'à liste triée

### Complexité
- **Pire cas:** O(n²)
- **Meilleur cas:** O(n) si déjà trié
- **Espace:** O(1)

### Avantages / Inconvénients
✅ Simple à comprendre et implémenter
✅ Tri en place (pas de mémoire supplémentaire)
❌ Très lent pour grandes listes
❌ Inefficace même pour listes presque triées

## Tri par sélection (Selection Sort)

### Principe
Trouve le minimum et le place au début, répète pour le reste.

### Algorithme
1. Trouver le plus petit élément
2. L'échanger avec le premier élément
3. Recommencer avec le reste de la liste

### Complexité
- **Toujours:** O(n²)
- **Espace:** O(1)

### Avantages / Inconvénients
✅ Simple
✅ Peu d'échanges (n au maximum)
❌ Toujours O(n²), même si déjà trié

## Tri par insertion (Insertion Sort)

### Principe
Construit la liste triée élément par élément, comme trier des cartes.

### Algorithme
1. Prendre un élément
2. L'insérer à la bonne place dans la partie triée
3. Répéter pour tous les éléments

### Complexité
- **Pire cas:** O(n²)
- **Meilleur cas:** O(n) si déjà trié
- **Espace:** O(1)

### Avantages / Inconvénients
✅ Efficace pour petites listes
✅ Efficace si liste presque triée
✅ Tri stable (garde l'ordre des égaux)
❌ O(n²) dans le pire cas

## Tri fusion (Merge Sort)

### Principe
**Diviser pour régner:** Divise en deux, trie chaque moitié, fusionne.

### Algorithme
1. Si liste ≤ 1 élément: déjà triée
2. Diviser en deux moitiés
3. Trier récursivement chaque moitié
4. Fusionner les deux moitiés triées

### Complexité
- **Toujours:** O(n log n) 🚀
- **Espace:** O(n)

### Avantages / Inconvénients
✅ Toujours O(n log n)
✅ Tri stable
✅ Prévisible
❌ Nécessite O(n) mémoire supplémentaire

## Comparaison

| Tri | Complexité | Mémoire | Stable |
|-----|------------|---------|--------|
| Bulles | O(n²) | O(1) | ✓ |
| Sélection | O(n²) | O(1) | ✗ |
| Insertion | O(n²) | O(1) | ✓ |
| Fusion | O(n log n) | O(n) | ✓ |
| Python (Timsort) | O(n log n) | O(n) | ✓ |""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Pratique: Implémentation des tris",
            content_markdown="""import random
import time

# Tri à bulles
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        echange = False
        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange = True
        if not echange:  # Optimisation: déjà trié
            break
    return liste

# Tri par sélection
def tri_selection(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

# Tri par insertion
def tri_insertion(liste):
    for i in range(1, len(liste)):
        element = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > element:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element
    return liste

# Tri fusion
def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    
    return fusionner(gauche, droite)

def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

# Tests
print("=== DÉMONSTRATION DES TRIS ===\n")

# Petite liste pour visualiser
liste_test = [64, 34, 25, 12, 22, 11, 90]
print(f"Liste initiale: {liste_test}\n")

print(f"Tri à bulles:    {tri_bulles(liste_test.copy())}")
print(f"Tri sélection:   {tri_selection(liste_test.copy())}")
print(f"Tri insertion:   {tri_insertion(liste_test.copy())}")
print(f"Tri fusion:      {tri_fusion(liste_test.copy())}")
print(f"Tri Python:      {sorted(liste_test)}")

# Comparaison de performance
print("\n=== COMPARAISON DE PERFORMANCE ===\n")

tailles = [10, 50, 100, 500]

for taille in tailles:
    liste = [random.randint(1, 1000) for _ in range(taille)]
    
    # Tri à bulles
    debut = time.time()
    tri_bulles(liste.copy())
    temps_bulles = (time.time() - debut) * 1000
    
    # Tri fusion
    debut = time.time()
    tri_fusion(liste.copy())
    temps_fusion = (time.time() - debut) * 1000
    
    # Tri Python
    debut = time.time()
    sorted(liste)
    temps_python = (time.time() - debut) * 1000
    
    print(f"n={taille:4} | Bulles: {temps_bulles:6.2f}ms | "
          f"Fusion: {temps_fusion:6.2f}ms | "
          f"Python: {temps_python:6.2f}ms")

# Visualisation étape par étape
print("\n=== TRI À BULLES ÉTAPE PAR ÉTAPE ===")
liste = [5, 2, 8, 1, 9]
print(f"Début: {liste}")
n = len(liste)
etape = 1
for i in range(n):
    for j in range(n - 1 - i):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]
            print(f"Étape {etape}: {liste}")
            etape += 1
print(f"Fin:   {liste}")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Tri personnalisé",
            content_markdown="""Implémente une fonction de tri pour trier une liste de **dictionnaires** par une clé spécifique.

**Exemple:**
```python
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 18},
    {"nom": "Charlie", "note": 12}
]

# Trier par note (décroissant)
def trier_par_cle(liste, cle, decroissant=False):
    # Utilise le tri par insertion ou à bulles
    # Compare liste[i][cle] et liste[j][cle]
    pass

resultat = trier_par_cle(etudiants, "note", decroissant=True)
# Résultat attendu:
# [{"nom": "Bob", "note": 18},
#  {"nom": "Alice", "note": 15},
#  {"nom": "Charlie", "note": 12}]
```

**Bonus:** Ajoute une option pour trier par plusieurs clés (ex: par note, puis par nom si égalité)!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz: Algorithmes de tri",
            content_markdown="""**Question 1:** Quel tri a toujours une complexité O(n log n)?
- a) Tri à bulles
- b) Tri par sélection
- c) Tri par insertion
- d) Tri fusion ✓

**Question 2:** Quel tri est le plus efficace pour une liste presque triée?
- a) Tri à bulles
- b) Tri par insertion ✓
- c) Tri par sélection
- d) Tous équivalents

**Question 3:** Qu'est-ce qu'un tri "stable"?
- a) Qui ne plante pas
- b) Qui est rapide
- c) Qui garde l'ordre des éléments égaux ✓
- d) Qui utilise peu de mémoire

**Question 4:** Combien de comparaisons au minimum pour trier 5 éléments?
- a) 5
- b) 7 ✓
- c) 10
- d) 25""",
            order=4
        )
        
        # Chapter 3: Algorithmes de recherche
        chapter3 = Chapter.objects.create(
            course=course,
            title="Algorithmes de recherche",
            description="Trouver efficacement un élément",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les algorithmes de recherche",
            content_markdown="""## Recherche linéaire (séquentielle)

### Principe
Parcourt la liste élément par élément jusqu'à trouver la valeur.

### Algorithme
```
Pour chaque élément de la liste:
    Si élément == valeur cherchée:
        Retourner l'index
    Sinon:
        Continuer
Retourner -1 (non trouvé)
```

### Complexité
- **Pire cas:** O(n) - élément à la fin ou absent
- **Meilleur cas:** O(1) - élément au début
- **Moyenne:** O(n/2) = O(n)

### Avantages / Inconvénients
✅ Fonctionne sur liste **non triée**
✅ Simple à implémenter
✅ Pas de préparation nécessaire
❌ Lent pour grandes listes

## Recherche dichotomique (binaire)

### Principe
**Diviser pour régner** sur une liste **triée**: compare avec l'élément du milieu.

### Algorithme
```
gauche = 0, droite = longueur - 1

Tant que gauche <= droite:
    milieu = (gauche + droite) // 2
    
    Si liste[milieu] == valeur:
        Retourner milieu
    
    Si liste[milieu] < valeur:
        gauche = milieu + 1  # Chercher à droite
    
    Sinon:
        droite = milieu - 1  # Chercher à gauche

Retourner -1 (non trouvé)
```

### Complexité
- **Toujours:** O(log n) 🚀
- **Espace:** O(1)

### Exemple de recherche

Liste triée: `[2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]`
Chercher: `23`

| Étape | Gauche | Droite | Milieu | Valeur | Action |
|-------|--------|--------|--------|--------|--------|
| 1 | 0 | 10 | 5 | 23 | **Trouvé!** ✓ |

Chercher: `45`

| Étape | Gauche | Droite | Milieu | Valeur | Action |
|-------|--------|--------|--------|--------|--------|
| 1 | 0 | 10 | 5 | 23 | 45 > 23 → droite |
| 2 | 6 | 10 | 8 | 56 | 45 < 56 → gauche |
| 3 | 6 | 7 | 6 | 38 | 45 > 38 → droite |
| 4 | 7 | 7 | 7 | 45 | **Trouvé!** ✓ |

### Avantages / Inconvénients
✅ **Très rapide:** O(log n)
✅ Efficace pour grandes listes
❌ Nécessite liste **triée**
❌ Un peu plus complexe à implémenter

## Comparaison

Pour une liste de **1 million** d'éléments:

| Algorithme | Opérations max | Temps estimé |
|------------|----------------|--------------|
| Linéaire | 1 000 000 | ~10 ms |
| Dichotomique | 20 | ~0.0002 ms |

**Gain:** 50 000 fois plus rapide! 🚀

## Quand utiliser quoi?

### Recherche linéaire
- Liste **non triée**
- Petite liste (< 100 éléments)
- Recherche ponctuelle
- Liste mise à jour fréquemment

### Recherche dichotomique
- Liste **triée**
- Grande liste (> 1000 éléments)
- Recherches multiples
- Liste stable (peu de modifications)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Pratique: Recherche linéaire vs dichotomique",
            content_markdown="""import time
import random

# Recherche linéaire
def recherche_lineaire(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i  # Index trouvé
    return -1  # Non trouvé

# Recherche dichotomique
def recherche_dichotomique(liste_triee, valeur):
    gauche = 0
    droite = len(liste_triee) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        
        if liste_triee[milieu] == valeur:
            return milieu
        elif liste_triee[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1

# Recherche dichotomique avec traces
def recherche_dichotomique_trace(liste_triee, valeur):
    gauche = 0
    droite = len(liste_triee) - 1
    etape = 1
    
    print(f"\nRecherche de {valeur} dans {liste_triee}")
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        print(f"Étape {etape}: gauche={gauche}, droite={droite}, "
              f"milieu={milieu}, valeur={liste_triee[milieu]}")
        
        if liste_triee[milieu] == valeur:
            print(f"✓ Trouvé à l'index {milieu}!")
            return milieu
        elif liste_triee[milieu] < valeur:
            print(f"  → {valeur} > {liste_triee[milieu]}, chercher à droite")
            gauche = milieu + 1
        else:
            print(f"  → {valeur} < {liste_triee[milieu]}, chercher à gauche")
            droite = milieu - 1
        
        etape += 1
    
    print("✗ Non trouvé")
    return -1

# Démonstration avec traces
print("=== RECHERCHE DICHOTOMIQUE DÉTAILLÉE ===")
liste = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
recherche_dichotomique_trace(liste, 45)
recherche_dichotomique_trace(liste, 100)

# Comparaison de performance
print("\n=== COMPARAISON DE PERFORMANCE ===\n")

tailles = [100, 1000, 10000, 100000]

for taille in tailles:
    # Créer une liste triée
    liste = sorted([random.randint(1, taille * 10) for _ in range(taille)])
    valeur = liste[random.randint(0, taille - 1)]  # Valeur existante
    
    # Recherche linéaire
    debut = time.time()
    idx1 = recherche_lineaire(liste, valeur)
    temps_lineaire = (time.time() - debut) * 1000000  # microsecondes
    
    # Recherche dichotomique
    debut = time.time()
    idx2 = recherche_dichotomique(liste, valeur)
    temps_dicho = (time.time() - debut) * 1000000
    
    gain = temps_lineaire / temps_dicho if temps_dicho > 0 else 0
    
    print(f"n={taille:6} | Linéaire: {temps_lineaire:8.2f} µs | "
          f"Dicho: {temps_dicho:8.2f} µs | Gain: x{gain:6.0f}")

# Exemple pratique: annuaire téléphonique
print("\n=== ANNUAIRE TÉLÉPHONIQUE ===")

annuaire = [
    "Alice", "Bernard", "Charlotte", "David", "Emma",
    "François", "Gabrielle", "Henri", "Isabelle", "Jacques"
]

nom_cherche = "Henri"
index = recherche_dichotomique(annuaire, nom_cherche)

if index != -1:
    print(f"✓ {nom_cherche} trouvé en position {index + 1}")
else:
    print(f"✗ {nom_cherche} non trouvé")

# Compter le nombre d'opérations
def compter_operations_dicho(n):
    return int(n.bit_length())  # log₂(n) arrondi

print("\n=== NOMBRE D'OPÉRATIONS MAXIMALES ===")
for n in [10, 100, 1000, 10000, 100000, 1000000]:
    ops = compter_operations_dicho(n)
    print(f"n={n:7} → max {ops:2} opérations")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Exercice: Recherche dans un annuaire",
            content_markdown="""Crée un système de recherche dans un **annuaire** avec noms et numéros de téléphone.

**Fonctionnalités:**
1. Stocker des contacts (nom, téléphone)
2. Rechercher par nom (dichotomique)
3. Afficher le numéro si trouvé
4. Gérer les ajouts (garder la liste triée)

**Structure:**
```python
contacts = [
    {"nom": "Alice", "tel": "06 12 34 56 78"},
    {"nom": "Bob", "tel": "06 98 76 54 32"},
    {"nom": "Charlie", "tel": "07 11 22 33 44"}
]

def rechercher_contact(contacts, nom):
    # Implémente la recherche dichotomique
    # Retourne le dictionnaire complet si trouvé
    pass

def ajouter_contact(contacts, nom, tel):
    # Ajoute et garde la liste triée par nom
    pass

# Test
contact = rechercher_contact(contacts, "Bob")
if contact:
    print(f"Téléphone de {contact['nom']}: {contact['tel']}")
```

**Bonus:** Ajoute la recherche par **préfixe** (ex: "Al" trouve "Alice", "Aline", etc.)!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Recherche",
            content_markdown="""**Question 1:** Quelle est la complexité de la recherche dichotomique?
- a) O(n)
- b) O(log n) ✓
- c) O(n²)
- d) O(1)

**Question 2:** Quelle condition est nécessaire pour la recherche dichotomique?
- a) Liste triée ✓
- b) Liste de nombres
- c) Liste sans doublons
- d) Liste courte

**Question 3:** Dans une liste de 1024 éléments, combien d'étapes max pour la recherche dichotomique?
- a) 8
- b) 10 ✓
- c) 512
- d) 1024

**Question 4:** Quel algorithme utiliser pour chercher dans une liste non triée?
- a) Recherche dichotomique
- b) Recherche linéaire ✓
- c) Les deux fonctionnent
- d) Impossible""",
            order=4
        )
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ Created {course.chapters.count()} chapters with '
            f'{ContentBlock.objects.filter(chapter__course=course).count()} blocks'
        ))
