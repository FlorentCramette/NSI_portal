from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI Traitement de Donnees course content'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating NSI Traitement de Donnees content...")
        
        course = Course.objects.get(slug='nsi-1-traitement-donnees')
        course.chapters.all().delete()
        
        # Chapter 1: Tables de donnees
        chapter1 = Chapter.objects.create(
            course=course,
            title="Tables de donnees",
            description="Manipulation et analyse de tables de donnees structurees",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Les tables de donnees",
            content_markdown="""# Tables de donnees

## Qu'est-ce qu'une table de donnees ?

Une **table de donnees** est une structure organisee en **lignes** et **colonnes** :
- **Lignes** : Representent des **enregistrements** (ex: une personne, un produit)
- **Colonnes** : Representent des **attributs** (ex: nom, age, prix)

## Formats de fichiers

### CSV (Comma-Separated Values)

Format texte simple ou les valeurs sont separees par des virgules :

```csv
nom,prenom,age,ville
Dupont,Marie,25,Paris
Martin,Pierre,30,Lyon
```

Avantages :
- Simple et universel
- Lisible par l'humain
- Compatible avec tous les outils

### JSON (JavaScript Object Notation)

Format structure avec paires cle-valeur :

```json
[
  {"nom": "Dupont", "prenom": "Marie", "age": 25},
  {"nom": "Martin", "prenom": "Pierre", "age": 30}
]
```

Avantages :
- Structure hierarchique
- Support des types (nombres, booleens)
- Tres utilise pour les APIs web

## Manipulation en Python

### Lecture CSV avec le module csv

```python
import csv

with open('donnees.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne['nom'], ligne['age'])
```

### Lecture JSON

```python
import json

with open('donnees.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for personne in data:
        print(personne['nom'])
```

## Operations sur les tables

### Selection (filtrage)

Extraire les lignes qui verifient une condition :

```python
adultes = [e for e in employes if int(e['age']) >= 18]
parisiens = [e for e in employes if e['ville'] == 'Paris']
```

### Projection

Selectionner uniquement certaines colonnes :

```python
noms_ages = [{k: e[k] for k in ['nom', 'age']} for e in employes]
```

### Tri

Ordonner les lignes selon un critere :

```python
employes_tries = sorted(employes, key=lambda e: int(e['age']))
```

### Agregation

Calculer des statistiques :

```python
ages = [int(e['age']) for e in employes]
age_moyen = sum(ages) / len(ages)
age_max = max(ages)
```""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Analyser des donnees CSV",
            content_markdown="""import csv
from collections import defaultdict

# Donnees CSV simulees
donnees_csv = '''nom,prenom,age,ville,salaire
Dupont,Marie,25,Paris,2500
Martin,Pierre,30,Lyon,3200
Durand,Sophie,28,Paris,2800
Bernard,Luc,35,Marseille,3500
Petit,Emma,26,Paris,2600'''

# Ecriture du fichier CSV
with open('employes.csv', 'w', encoding='utf-8') as f:
    f.write(donnees_csv)

# Lecture et analyse
print("ANALYSE DES DONNEES EMPLOYES\\n")

with open('employes.csv', 'r', encoding='utf-8') as f:
    lecteur = csv.DictReader(f)
    employes = list(lecteur)

# Affichage des donnees
print("Donnees brutes:")
for emp in employes:
    print(f"  {emp['prenom']} {emp['nom']}, {emp['age']} ans, {emp['ville']} - {emp['salaire']}E")

# 1. Filtrage : Employes de Paris
print("\\nEmployes a Paris:")
parisiens = [e for e in employes if e['ville'] == 'Paris']
for emp in parisiens:
    print(f"  {emp['prenom']} {emp['nom']} - {emp['salaire']}E")

# 2. Tri par age
print("\\nTri par age (croissant):")
employes_tries = sorted(employes, key=lambda e: int(e['age']))
for emp in employes_tries:
    print(f"  {emp['prenom']} {emp['nom']}: {emp['age']} ans")

# 3. Agregations
ages = [int(e['age']) for e in employes]
salaires = [int(e['salaire']) for e in employes]

print("\\nSTATISTIQUES:")
print(f"  Nombre d'employes: {len(employes)}")
print(f"  Age moyen: {sum(ages) / len(ages):.1f} ans")
print(f"  Age minimum: {min(ages)} ans")
print(f"  Age maximum: {max(ages)} ans")
print(f"  Salaire moyen: {sum(salaires) / len(salaires):.0f}E")

# 4. Groupement par ville
print("\\nREPARTITION PAR VILLE:")
par_ville = defaultdict(list)
for emp in employes:
    par_ville[emp['ville']].append(emp)

for ville, employes_ville in par_ville.items():
    salaires_ville = [int(e['salaire']) for e in employes_ville]
    print(f"  {ville}: {len(employes_ville)} employes, salaire moyen: {sum(salaires_ville) / len(salaires_ville):.0f}E")

# 5. Employes avec salaire > 3000E
print("\\nEmployes avec salaire > 3000E:")
hauts_salaires = [e for e in employes if int(e['salaire']) > 3000]
for emp in hauts_salaires:
    print(f"  {emp['prenom']} {emp['nom']}: {emp['salaire']}E")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz : Tables de donnees",
            content_markdown="""**Question 1:** Que represente une ligne dans une table de donnees ?
- a) Un attribut
- b) Une colonne
- c) Un enregistrement ✓
- d) Un fichier

**Question 2:** Quel format permet une structure hierarchique ?
- a) CSV
- b) JSON ✓
- c) TXT
- d) Les deux

**Question 3:** Quelle operation permet de ne garder que certaines colonnes ?
- a) Selection
- b) Projection ✓
- c) Tri
- d) Agregation

**Question 4:** Que calcule une moyenne ?
- a) Le maximum
- b) La mediane
- c) La somme divisee par le nombre d'elements ✓
- d) Le total""",
            order=3
        )
        
        # Chapter 2: Recherche et tri dans les donnees
        chapter2 = Chapter.objects.create(
            course=course,
            title="Recherche et tri dans les donnees",
            description="Algorithmes de recherche et de tri appliques aux tables",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Recherche dans les donnees",
            content_markdown="""# Recherche et tri dans les donnees

## Recherche dans une table

### Recherche simple (lineaire)

Parcourir tous les enregistrements pour trouver une correspondance :

```python
def rechercher_par_nom(table, nom_recherche):
    resultats = []
    for enregistrement in table:
        if enregistrement['nom'] == nom_recherche:
            resultats.append(enregistrement)
    return resultats
```

**Complexite** : O(n) - proportionnelle au nombre d'enregistrements

### Recherche avec criteres multiples

```python
def rechercher_avance(table, ville=None, age_min=None):
    resultats = table
    if ville:
        resultats = [e for e in resultats if e['ville'] == ville]
    if age_min:
        resultats = [e for e in resultats if int(e['age']) >= age_min]
    return resultats
```

## Tri des donnees

### Tri simple avec Python

```python
# Tri simple
table_triee = sorted(table, key=lambda x: x['age'])

# Tri decroissant
table_triee = sorted(table, key=lambda x: x['salaire'], reverse=True)

# Tri sur plusieurs criteres
table_triee = sorted(table, key=lambda x: (x['ville'], x['age']))
```

## Index pour accelerer les recherches

Un **index** est une structure de donnees auxiliaire qui accelere les recherches :

```python
def creer_index(table, cle):
    index = {}
    for i, enreg in enumerate(table):
        valeur = enreg[cle]
        if valeur not in index:
            index[valeur] = []
        index[valeur].append(i)
    return index

# Utilisation
index_ville = creer_index(employes, 'ville')
# Recherche rapide O(1) au lieu de O(n)
positions_paris = index_ville.get('Paris', [])
```

## Optimisation des requetes

### Eviter les boucles imbriquees

Inefficace O(n2) :
```python
for emp1 in employes:
    for emp2 in employes:
        if emp1['ville'] == emp2['ville']:
            pass  # O(n2) !
```

Efficace O(n) :
```python
par_ville = {}
for emp in employes:
    ville = emp['ville']
    if ville not in par_ville:
        par_ville[ville] = []
    par_ville[ville].append(emp)
```

### Utiliser des structures appropriees

- **Liste** : Acces sequentiel
- **Dictionnaire** : Recherche rapide par cle O(1)
- **Set** : Test d'appartenance rapide O(1)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Moteur de recherche de produits",
            content_markdown="""import time
from collections import defaultdict

# Base de donnees de produits
produits = [
    {"id": 1, "nom": "iPhone 15", "categorie": "Telephone", "prix": 999, "stock": 50},
    {"id": 2, "nom": "Samsung Galaxy S24", "categorie": "Telephone", "prix": 899, "stock": 30},
    {"id": 3, "nom": "MacBook Pro", "categorie": "Ordinateur", "prix": 2499, "stock": 20},
    {"id": 4, "nom": "Dell XPS 13", "categorie": "Ordinateur", "prix": 1299, "stock": 15},
    {"id": 5, "nom": "iPad Air", "categorie": "Tablette", "prix": 699, "stock": 40},
    {"id": 6, "nom": "AirPods Pro", "categorie": "Audio", "prix": 279, "stock": 100},
    {"id": 7, "nom": "Sony WH-1000XM5", "categorie": "Audio", "prix": 399, "stock": 25},
    {"id": 8, "nom": "Apple Watch", "categorie": "Montre", "prix": 449, "stock": 60},
]

# 1. Recherche lineaire simple
def recherche_lineaire(nom_partiel):
    resultats = []
    for produit in produits:
        if nom_partiel.lower() in produit['nom'].lower():
            resultats.append(produit)
    return resultats

# 2. Creation d'index pour recherche rapide
def creer_index_categorie():
    index = defaultdict(list)
    for produit in produits:
        index[produit['categorie']].append(produit)
    return index

# 3. Recherche multi-criteres
def recherche_avancee(categorie=None, prix_min=None, prix_max=None):
    resultats = produits.copy()
    if categorie:
        resultats = [p for p in resultats if p['categorie'] == categorie]
    if prix_min is not None:
        resultats = [p for p in resultats if p['prix'] >= prix_min]
    if prix_max is not None:
        resultats = [p for p in resultats if p['prix'] <= prix_max]
    return resultats

# 4. Tri des resultats
def trier_produits(produits_list, critere='prix', ordre='croissant'):
    reverse = (ordre == 'decroissant')
    return sorted(produits_list, key=lambda p: p[critere], reverse=reverse)

# Demonstration
print("MOTEUR DE RECHERCHE DE PRODUITS\\n")

# Recherche simple
print("Recherche 'Phone':")
resultats = recherche_lineaire('Phone')
for p in resultats:
    print(f"  {p['nom']} - {p['prix']}E (stock: {p['stock']})")

# Index par categorie
print("\\nIndex par categorie:")
index = creer_index_categorie()
for cat, prods in index.items():
    print(f"  {cat}: {len(prods)} produits")

# Recherche dans une categorie
print("\\nProduits Telephone:")
for p in index['Telephone']:
    print(f"  {p['nom']} - {p['prix']}E")

# Recherche multi-criteres
print("\\nRecherche avancee (Audio, prix < 350E):")
resultats = recherche_avancee(categorie='Audio', prix_max=350)
for p in resultats:
    print(f"  {p['nom']} - {p['prix']}E")

# Tri par prix decroissant
print("\\nTop 5 produits les plus chers:")
produits_tries = trier_produits(produits, critere='prix', ordre='decroissant')
for p in produits_tries[:5]:
    print(f"  {p['nom']} - {p['prix']}E")

# Statistiques globales
print("\\nSTATISTIQUES:")
prix_total = sum(p['prix'] for p in produits)
stock_total = sum(p['stock'] for p in produits)
print(f"  Nombre de produits: {len(produits)}")
print(f"  Prix moyen: {prix_total / len(produits):.0f}E")
print(f"  Stock total: {stock_total} unites")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz : Recherche et tri",
            content_markdown="""**Question 1:** Quelle est la complexite d'une recherche lineaire ?
- a) O(1)
- b) O(log n)
- c) O(n) ✓
- d) O(n2)

**Question 2:** A quoi sert un index dans une table de donnees ?
- a) A trier les donnees
- b) A accelerer les recherches ✓
- c) A supprimer les doublons
- d) A calculer des statistiques

**Question 3:** Quelle complexite a le tri fusion ?
- a) O(n)
- b) O(n log n) ✓
- c) O(n2)
- d) O(log n)

**Question 4:** Quelle structure est la plus rapide pour tester l'appartenance ?
- a) Liste
- b) Tableau
- c) Set ✓
- d) Tuple""",
            order=3
        )
        
        # Chapter 3: Visualisation de donnees
        chapter3 = Chapter.objects.create(
            course=course,
            title="Visualisation de donnees",
            description="Creer des graphiques et representations visuelles des donnees",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Visualiser les donnees",
            content_markdown="""# Visualisation de donnees

## Pourquoi visualiser ?

La visualisation transforme des donnees numeriques en representations visuelles pour :
- **Comprendre** les tendances et patterns
- **Communiquer** les resultats efficacement
- **Detecter** les anomalies
- **Comparer** des valeurs

## Types de graphiques

### 1. Graphique en barres

Pour comparer des categories :

**Usage** : Comparaison de categories discretes

### 2. Histogramme

Pour visualiser la distribution d'une variable continue.

**Usage** : Repartition d'une variable numerique

### 3. Graphique en ligne

Pour montrer l'evolution dans le temps.

**Usage** : Series temporelles, evolutions

### 4. Graphique circulaire (camembert)

Pour montrer des proportions d'un tout (100%).

### 5. Nuage de points (scatter plot)

Pour visualiser la correlation entre deux variables.

**Usage** : Relations entre variables

## Principes de visualisation

### Bonnes pratiques

1. **Choisir le bon type** de graphique selon les donnees
2. **Titrer** clairement le graphique et les axes
3. **Utiliser des couleurs** harmonieuses et accessibles
4. **Eviter la surcharge** d'informations
5. **Commencer l'axe Y a zero** (sauf cas particuliers)

### Pieges a eviter

- Axe Y ne commencant pas a zero (exagere les differences)
- Trop de categories sur un meme graphique
- Graphique en 3D sans raison (difficile a lire)
- Couleurs inappropriees (rouge/vert pour daltoniens)

## Visualisation en Python

### Avec matplotlib

```python
import matplotlib.pyplot as plt

# Donnees
categories = ['A', 'B', 'C', 'D']
valeurs = [25, 40, 30, 15]

# Graphique en barres
plt.bar(categories, valeurs)
plt.title('Repartition par categorie')
plt.xlabel('Categorie')
plt.ylabel('Valeur')
plt.show()

# Graphique en ligne
dates = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven']
temperatures = [18, 20, 22, 19, 21]
plt.plot(dates, temperatures, marker='o')
plt.title('Temperature de la semaine')
plt.show()
```

## Interpretation des graphiques

### Tendances

- **Croissante** : Les valeurs augmentent
- **Decroissante** : Les valeurs diminuent
- **Stable** : Pas de variation significative
- **Cyclique** : Repetition de patterns

### Correlation

- **Positive** : Les deux variables augmentent ensemble
- **Negative** : Quand l'une augmente, l'autre diminue
- **Nulle** : Pas de relation apparente""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Creer des visualisations ASCII",
            content_markdown="""# Visualisation de donnees en mode texte (ASCII)

def graphique_barres(donnees, largeur_max=40):
    # Cree un graphique en barres ASCII
    if not donnees:
        return
    
    max_val = max(donnees.values())
    max_label = max(len(str(k)) for k in donnees.keys())
    
    print("\\nGRAPHIQUE EN BARRES\\n")
    for label, valeur in donnees.items():
        longueur = int((valeur / max_val) * largeur_max)
        barre = '#' * longueur
        print(f"{str(label):<{max_label}} | {barre} {valeur}")
    print("-" * (max_label + largeur_max + 10))

def camembert(donnees):
    # Representation textuelle d'un camembert
    total = sum(donnees.values())
    
    print("\\nGRAPHIQUE CIRCULAIRE\\n")
    for label, valeur in donnees.items():
        pourcentage = (valeur / total) * 100
        nb_symboles = int(pourcentage / 2)
        barre = '#' * nb_symboles
        print(f"{label:<15} {barre} {pourcentage:.1f}%")

# Demonstrations
print("=" * 60)
print("VISUALISATIONS DE DONNEES")
print("=" * 60)

# 1. Graphique en barres - Ventes par mois
ventes = {
    'Janvier': 45000,
    'Fevrier': 52000,
    'Mars': 48000,
    'Avril': 61000,
    'Mai': 58000,
    'Juin': 67000
}
graphique_barres(ventes)

# 2. Camembert - Repartition du budget
budget = {
    'Logement': 800,
    'Alimentation': 400,
    'Transport': 200,
    'Loisirs': 150,
    'Epargne': 250,
    'Divers': 200
}
camembert(budget)

# 3. Statistiques resumees
print("\\nSTATISTIQUES DETAILLEES\\n")
print("Ventes mensuelles:")
print(f"  Total: {sum(ventes.values())} E")
print(f"  Moyenne: {sum(ventes.values())/len(ventes):.0f} E")
print(f"  Maximum: {max(ventes.values())} E ({max(ventes, key=ventes.get)})")
print(f"  Minimum: {min(ventes.values())} E ({min(ventes, key=ventes.get)})")

# 4. Evolution simple en texte
print("\\nEVOLUTION MENSUELLE:")
mois_precedent = None
for mois, valeur in ventes.items():
    if mois_precedent:
        evolution = valeur - mois_precedent
        symbole = "+" if evolution > 0 else ""
        print(f"  {mois}: {valeur} E ({symbole}{evolution})")
    else:
        print(f"  {mois}: {valeur} E")
    mois_precedent = valeur""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz : Visualisation",
            content_markdown="""**Question 1:** Quel graphique est adapte pour montrer l'evolution dans le temps ?
- a) Graphique en barres
- b) Graphique en ligne ✓
- c) Camembert
- d) Histogramme

**Question 2:** Que montre un histogramme ?
- a) L'evolution temporelle
- b) La distribution d'une variable ✓
- c) Les proportions d'un tout
- d) La correlation entre variables

**Question 3:** Quel graphique utilise-t-on pour montrer des proportions totalisant 100% ?
- a) Barres
- b) Ligne
- c) Camembert ✓
- d) Nuage de points

**Question 4:** Quelle est une bonne pratique en visualisation ?
- a) Utiliser le plus de couleurs possible
- b) Commencer l'axe Y a zero ✓
- c) Ajouter des effets 3D partout
- d) Mettre beaucoup de donnees sur un graphique

**Question 5:** Que revele un nuage de points ?
- a) L'evolution temporelle
- b) Les proportions
- c) La correlation entre deux variables ✓
- d) La distribution""",
            order=3
        )
        
        blocks_count = sum(ch.content_blocks.count() for ch in [chapter1, chapter2, chapter3])
        self.stdout.write(
            self.style.SUCCESS(f'Created 3 chapters with {blocks_count} blocks for NSI Traitement de Donnees')
        )
