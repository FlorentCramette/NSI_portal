from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Photographie Numérique course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Photographie Numérique course content...')
        
        try:
            course = Course.objects.get(slug='snt-photo-numerique')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Photo Numérique not found'))
            return
        
        course.chapters.all().delete()
        
        # Chapter 1: Photographie argentique vs numérique
        chapter1 = Chapter.objects.create(
            course=course,
            title="De l'argentique au numérique",
            description="Comprendre la révolution de la photographie numérique",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Histoire de la photographie",
            content_markdown="""## La photographie argentique (1826-2000)

### Fonctionnement
- **Support**: Pellicule contenant des sels d'argent sensibles à la lumière
- **Développement**: Processus chimique en chambre noire
- **Coût**: Chaque photo coûte de l'argent (pellicule + développement)
- **Nombre limité**: 24 ou 36 photos par pellicule

### Avantages ✅
- Qualité d'image exceptionnelle
- Durabilité physique des tirages
- Réflexion avant de photographier

### Inconvénients ❌
- Coût élevé
- Pas de prévisualisation instantanée
- Stockage physique encombrant
- Partage difficile

## La photographie numérique (2000 - aujourd'hui)

### Fonctionnement
- **Capteur**: Composant électronique (CCD ou CMOS)
- **Traitement**: Processeur convertit en image numérique
- **Stockage**: Carte mémoire (SD, microSD...)
- **Format**: JPEG, RAW, PNG...

### Révolution
- 📱 **2000**: Premier téléphone avec appareil photo
- 📸 **2007**: iPhone popularise la photo mobile
- 📷 **Aujourd'hui**: 1,8 trillion de photos par an!

### Avantages ✅
- Coût marginal nul après achat
- Prévisualisation instantanée
- Capacité illimitée
- Partage facile
- Retouche et filtres

### Inconvénients ❌
- Dépendance aux batteries
- Obsolescence rapide
- Perte de qualité si compression""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Histoire de la photo",
            content_markdown="""**Question 1:** Qu'est-ce qui remplace la pellicule dans un appareil numérique?
- a) Un miroir
- b) Un capteur électronique ✓
- c) Une lentille
- d) Un écran

**Question 2:** Combien de photos sont prises chaque année dans le monde?
- a) 100 millions
- b) 1 milliard
- c) 100 milliards
- d) 1,8 trillion ✓

**Question 3:** Quel est le principal avantage de la photo numérique?
- a) Elle est en couleur
- b) Elle coûte moins cher à produire ✓
- c) Elle est plus lourde
- d) Elle nécessite une chambre noire""",
            order=2
        )
        
        # Chapter 2: Les pixels et la résolution
        chapter2 = Chapter.objects.create(
            course=course,
            title="Pixels et résolution d'image",
            description="Comprendre comment sont codées les images numériques",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Qu'est-ce qu'un pixel?",
            content_markdown="""## Le pixel: unité de base

Un **pixel** (Picture Element) est le plus petit point qui compose une image numérique.

### Caractéristiques d'un pixel:
- Contient une **couleur unique**
- Codé en **RGB** (Rouge, Vert, Bleu)
- Chaque composante: 0 à 255 (256 valeurs)
- Total: 256³ = **16,7 millions de couleurs**

### Exemples de couleurs RGB:
| Couleur | R | G | B | Code |
|---------|---|---|---|------|
| Noir | 0 | 0 | 0 | (0, 0, 0) |
| Blanc | 255 | 255 | 255 | (255, 255, 255) |
| Rouge | 255 | 0 | 0 | (255, 0, 0) |
| Vert | 0 | 255 | 0 | (0, 255, 0) |
| Bleu | 0 | 0 | 255 | (0, 0, 255) |
| Jaune | 255 | 255 | 0 | (255, 255, 0) |

## La résolution

**Résolution** = nombre de pixels (largeur × hauteur)

### Exemples:
- **HD**: 1280 × 720 = 0,9 MP
- **Full HD**: 1920 × 1080 = 2 MP
- **4K**: 3840 × 2160 = 8,3 MP
- **iPhone 15**: 4032 × 3024 = 12 MP

### Poids d'une image
**Image Full HD non compressée:**
- 1920 × 1080 = 2 073 600 pixels
- 3 octets par pixel (RGB)
- **Total**: 6,2 Mo
- **Avec JPEG**: ~500 Ko (divisé par 12!)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exemple Python: Créer un dégradé de couleur",
            content_markdown="""# Créons une image avec un dégradé de bleu

def creer_degrade_bleu(largeur, hauteur):
    # Image = liste de lignes, chaque ligne = liste de pixels
    image = []
    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            # Dégradé: de noir à bleu pur
            intensite_bleu = int((x / largeur) * 255)
            pixel = (0, 0, intensite_bleu)  # RGB
            ligne.append(pixel)
        image.append(ligne)
    return image

# Créer une petite image 10x10
image = creer_degrade_bleu(10, 10)

print("Image 10x10 pixels - Dégradé de bleu:")
print(f"Pixel gauche: {image[0][0]}")   # (0, 0, 0) = noir
print(f"Pixel milieu: {image[0][5]}")   # (0, 0, 127) = bleu moyen
print(f"Pixel droite: {image[0][9]}")   # (0, 0, 255) = bleu pur

# Calculer la taille
nb_pixels = 10 * 10
taille_octets = nb_pixels * 3
print(f"\\nTaille: {taille_octets} octets")

# Pour une vraie photo
largeur, hauteur = 4032, 3024
megapixels = (largeur * hauteur) / 1_000_000
taille_mo = (largeur * hauteur * 3) / 1_000_000
print(f"\\nPhoto {largeur}x{hauteur}:")
print(f"  {megapixels:.1f} mégapixels")
print(f"  {taille_mo:.1f} Mo non compressée")
print(f"  ~{taille_mo/12:.1f} Mo en JPEG")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Calculateur de taille d'image",
            content_markdown="""Crée un programme qui calcule la taille d'une image.

**Entrées:**
- Largeur en pixels
- Hauteur en pixels

**Calculs:**
1. Nombre total de pixels
2. Taille non compressée (3 octets/pixel)
3. Taille JPEG estimée (divisé par 12)
4. Combien de photos sur une carte SD 32 Go

**Exemple de sortie:**
```
Largeur: 4000 pixels
Hauteur: 3000 pixels

Résultats:
• 12,000,000 pixels (12 MP)
• Taille brute: 36.0 Mo
• Taille JPEG: ~3.0 Mo

Sur une carte SD 32 Go:
→ Environ 10,900 photos
```""",
            order=3
        )
        
        # Chapter 3: Formats d'image
        chapter3 = Chapter.objects.create(
            course=course,
            title="Formats et compression d'images",
            description="Comprendre JPEG, PNG, RAW et la compression",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les formats d'image",
            content_markdown="""## Formats sans perte (lossless)

### PNG
- ✅ Qualité parfaite préservée
- ✅ Transparence supportée
- ✅ Idéal pour: logos, graphiques
- ❌ Fichiers plus lourds

### RAW
- ✅ Données brutes du capteur
- ✅ Maximum de qualité
- ✅ Utilisé par les pros
- ❌ Très lourd (20-50 Mo)
- ❌ Logiciel spécial requis

## Formats avec perte (lossy)

### JPEG
- ✅ **Le plus utilisé** (90% des photos)
- ✅ Compression efficace (÷10-20)
- ✅ Compatible partout
- ❌ Perte de qualité irréversible
- ❌ Pas de transparence

**Niveaux de qualité JPEG:**
| Qualité | Poids | Usage |
|---------|-------|-------|
| 100% | 5 Mo | Professionnel |
| 85% | 1 Mo | Haute qualité ⭐ |
| 70% | 500 Ko | Web |
| 50% | 200 Ko | Miniatures |

### WebP
- ✅ Format moderne Google
- ✅ 25-35% plus léger que JPEG
- ✅ Transparence OK
- ❌ Moins compatible

## Compression JPEG

**Comment ça marche:**
1. Découpe l'image en blocs 8×8
2. Convertit RGB → YCbCr (luminance + couleur)
3. Supprime détails invisibles
4. Stockage compact

⚠️ Chaque sauvegarde JPEG dégrade un peu plus!""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Exemple: Simuler la compression",
            content_markdown="""# Simulation de compression d'image

def comprimer_image(nb_pixels, taux_compression):
    # taux_compression: 1 = max qualité, 10 = min qualité
    poids_original = nb_pixels * 3
    pixels_gardes = nb_pixels // taux_compression
    poids_compresse = pixels_gardes * 3
    
    gain = (1 - poids_compresse / poids_original) * 100
    ratio = poids_original / poids_compresse
    
    print(f"Pixels originaux: {nb_pixels:,}")
    print(f"Taille originale: {poids_original/1024:.1f} Ko")
    print(f"\\nAprès compression (taux {taux_compression}):")
    print(f"  Pixels gardés: {pixels_gardes:,}")
    print(f"  Taille: {poids_compresse/1024:.1f} Ko")
    print(f"  Gain: {gain:.1f}%")
    print(f"  Ratio: {ratio:.1f}:1")

# Test avec une image 1000x1000
pixels = 1000 * 1000

print("=== COMPRESSION LÉGÈRE ===")
comprimer_image(pixels, 2)

print("\\n=== COMPRESSION MOYENNE ===")
comprimer_image(pixels, 5)

print("\\n=== COMPRESSION FORTE ===")
comprimer_image(pixels, 10)

# Comparaison des formats pour une photo 12 MP
print("\\n=== PHOTO 12 MP - FORMATS ===")
photo_12mp = 12_000_000
formats = {
    "RAW": 1.0,
    "PNG": 0.5,
    "JPEG 100%": 0.15,
    "JPEG 85%": 0.08,
    "JPEG 70%": 0.04,
    "WebP": 0.06
}

for nom, ratio in formats.items():
    taille = (photo_12mp * 3 * ratio) / 1_000_000
    print(f"{nom:12} : {taille:6.2f} Mo")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Formats et compression",
            content_markdown="""**Question 1:** Quel format est le plus utilisé pour les photos?
- a) PNG
- b) JPEG ✓
- c) BMP
- d) RAW

**Question 2:** Qu'est-ce qu'une compression "avec perte"?
- a) L'image est perdue
- b) Des détails sont supprimés pour réduire la taille ✓
- c) La couleur est perdue
- d) L'image devient floue

**Question 3:** Quel format supporte la transparence?
- a) JPEG
- b) PNG ✓
- c) Les deux
- d) Aucun

**Question 4:** Un fichier RAW est:
- a) Plus petit qu'un JPEG
- b) En noir et blanc
- c) Les données brutes du capteur ✓
- d) Un format obsolète""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
