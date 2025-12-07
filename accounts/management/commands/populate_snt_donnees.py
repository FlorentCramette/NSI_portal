from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Données Structurées course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Données Structurées course content...')
        
        # Get the course
        try:
            course = Course.objects.get(slug='snt-donnees-structurees')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Données Structurées not found'))
            return
        
        # Clear existing chapters
        course.chapters.all().delete()
        
        # Chapter 1: Introduction aux données
        chapter1 = Chapter.objects.create(
            course=course,
            title="Qu'est-ce qu'une donnée?",
            description="Comprendre ce qu'est une donnée et son importance",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Définition et types de données",
            content_markdown="""Une **donnée** est une information brute qui peut être traitée, analysée et utilisée.

## Types de données

### Données quantitatives (nombres)
- Âge: 15 ans
- Température: 22°C
- Prix: 49,99€

### Données qualitatives (texte, catégories)
- Prénom: "Alice"
- Couleur préférée: "Bleu"
- Ville: "Paris"

### Données booléennes (vrai/faux)
- Est majeur: False
- A le permis: False
- Aime le sport: True

## L'importance des données

À l'ère du numérique, les données sont partout:
- Réseaux sociaux (posts, likes, commentaires)
- Commerce (achats, historique)
- Santé (dossiers médicaux)
- Éducation (notes, présences)

Les données sont appelées **"le pétrole du 21ème siècle"** car elles ont une immense valeur.""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Exemple Python: Manipuler des données",
            content_markdown="""# Données d'un élève
eleve = {
    "prenom": "Alice",
    "age": 15,
    "classe": "2nde",
    "notes": [14, 16, 15, 17],
    "presente": True
}

# Accéder aux données
print(f"Élève: {eleve['prenom']}")
print(f"Âge: {eleve['age']} ans")
print(f"Classe: {eleve['classe']}")

# Calculer la moyenne
moyenne = sum(eleve['notes']) / len(eleve['notes'])
print(f"Moyenne: {moyenne:.1f}/20")

# Vérifier la présence
if eleve['presente']:
    print("✓ Présent(e)")
else:
    print("✗ Absent(e)")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Les données",
            content_markdown="""**Question 1:** Qu'est-ce qu'une donnée?
- a) Un programme informatique
- b) Une information brute qui peut être traitée ✓
- c) Un ordinateur
- d) Un réseau social

**Question 2:** Quel type de donnée est "15 ans"?
- a) Qualitative
- b) Quantitative ✓
- c) Booléenne
- d) Textuelle

**Question 3:** Pourquoi dit-on que les données sont "le pétrole du 21ème siècle"?
- a) Parce qu'elles polluent
- b) Parce qu'elles ont une grande valeur ✓
- c) Parce qu'elles sont noires
- d) Parce qu'elles sentent mauvais""",
            order=3
        )
        
        # Chapter 2: Tables et CSV
        chapter2 = Chapter.objects.create(
            course=course,
            title="Tables et fichiers CSV",
            description="Apprendre à organiser des données dans des tables",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les tables de données",
            content_markdown="""Une **table** est une façon d'organiser des données en lignes et colonnes, comme un tableau Excel.

## Structure d'une table

| Prénom | Âge | Classe | Moyenne |
|--------|-----|--------|---------|
| Alice  | 15  | 2nde A | 15.5    |
| Bob    | 16  | 2nde A | 13.2    |
| Claire | 15  | 2nde B | 16.8    |

### Vocabulaire:
- **Ligne** (ou enregistrement): Représente un individu/objet
- **Colonne** (ou champ): Représente une propriété
- **Cellule**: Intersection d'une ligne et d'une colonne

## Le format CSV

**CSV** (Comma-Separated Values) est un format de fichier texte pour stocker des tables:

```csv
prenom,age,classe,moyenne
Alice,15,2nde A,15.5
Bob,16,2nde A,13.2
Claire,15,2nde B,16.8
```

Caractéristiques:
- Première ligne = **en-têtes** (noms des colonnes)
- Lignes suivantes = **données**
- Valeurs séparées par des **virgules** (ou points-virgules)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exemple Python: Lire un fichier CSV",
            content_markdown="""import csv

# Données en mémoire (simule un fichier CSV)
donnees_csv = \"\"\"prenom,age,classe,moyenne
Alice,15,2nde A,15.5
Bob,16,2nde A,13.2
Claire,15,2nde B,16.8\"\"\"

# Parser le CSV
lignes = donnees_csv.strip().split('\\n')
reader = csv.DictReader(lignes)

# Afficher chaque élève
print("Liste des élèves:\\n")
for eleve in reader:
    print(f"{eleve['prenom']:8} | {eleve['age']} ans | {eleve['classe']:7} | Moyenne: {eleve['moyenne']}")

# Calculer des statistiques
lignes = donnees_csv.strip().split('\\n')
reader = csv.DictReader(lignes)
moyennes = [float(eleve['moyenne']) for eleve in reader]

print(f"\\nMoyenne de la classe: {sum(moyennes)/len(moyennes):.2f}")
print(f"Meilleure moyenne: {max(moyennes)}")
print(f"Plus basse moyenne: {min(moyennes)}")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Analyser des données CSV",
            content_markdown="""Tu as des données de ventes de livres en CSV:

```csv
titre,auteur,prix,exemplaires_vendus
Python,Guido,29.99,150
HTML/CSS,Jon,24.99,200
JavaScript,Douglas,34.99,120
```

Écris un programme Python qui:
1. Parse ces données
2. Calcule le **revenu total** pour chaque livre (prix × exemplaires vendus)
3. Affiche le livre qui a généré le plus de revenus

**Indice:**
```python
import csv

donnees = \"\"\"titre,auteur,prix,exemplaires_vendus
Python,Guido,29.99,150
HTML/CSS,Jon,24.99,200
JavaScript,Douglas,34.99,120\"\"\"

# Ton code ici
```""",
            order=3
        )
        
        # Chapter 3: JSON et données structurées
        chapter3 = Chapter.objects.create(
            course=course,
            title="Le format JSON",
            description="Découvrir JSON, le format de données du Web",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Qu'est-ce que JSON?",
            content_markdown="""**JSON** (JavaScript Object Notation) est un format léger et populaire pour échanger des données sur le Web.

## Structure JSON

```json
{
  "prenom": "Alice",
  "age": 15,
  "classe": "2nde A",
  "notes": [14, 16, 15, 17],
  "options": {
    "sport": true,
    "musique": false
  }
}
```

## Types de données en JSON

- **String** (chaîne): `"texte"`
- **Number** (nombre): `42`, `3.14`
- **Boolean**: `true`, `false`
- **Array** (liste): `[1, 2, 3]`
- **Object** (dictionnaire): `{"clé": "valeur"}`
- **null**: Valeur nulle

## JSON vs CSV

| Critère | CSV | JSON |
|---------|-----|------|
| Structure | Table plate | Hiérarchique |
| Complexité | Simple | Complexe possible |
| Usage | Tableurs, bases de données | APIs, configuration, Web |
| Lisibilité | Bonne | Très bonne |""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Exemple Python: Manipuler du JSON",
            content_markdown="""import json

# Données Python → JSON
eleve = {
    "prenom": "Alice",
    "age": 15,
    "classe": "2nde A",
    "notes": [14, 16, 15, 17],
    "presente": True
}

# Convertir en JSON
json_string = json.dumps(eleve, indent=2, ensure_ascii=False)
print("Données en JSON:")
print(json_string)

# JSON → Données Python
print("\\nDonnées parsées:")
donnees = json.loads(json_string)
print(f"Prénom: {donnees['prenom']}")
print(f"Notes: {donnees['notes']}")
print(f"Moyenne: {sum(donnees['notes']) / len(donnees['notes']):.1f}")

# Exemple d'API (données plus complexes)
api_response = '''
{
  "cours": "SNT",
  "eleves": [
    {"nom": "Alice", "moyenne": 15.5},
    {"nom": "Bob", "moyenne": 13.2}
  ],
  "nombre_eleves": 2
}
'''

data = json.loads(api_response)
print(f"\\nCours: {data['cours']}")
print(f"Nombre d'élèves: {data['nombre_eleves']}")
for eleve in data['eleves']:
    print(f"  - {eleve['nom']}: {eleve['moyenne']}/20")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Exercice: Créer une API météo",
            content_markdown="""Crée une structure JSON qui représente les prévisions météo pour 3 jours.

**Structure attendue:**
```json
{
  "ville": "Paris",
  "previsions": [
    {
      "jour": "Lundi",
      "temperature": 22,
      "conditions": "Ensoleillé",
      "pluie": false
    },
    ...
  ]
}
```

Ensuite, écris un programme Python qui:
1. Parse ce JSON
2. Affiche les prévisions de manière lisible
3. Calcule la température moyenne sur les 3 jours

**Bonus:** Indique quel jour il fera le plus chaud.""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
