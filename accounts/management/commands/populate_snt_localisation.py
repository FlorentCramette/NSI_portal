from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Localisation course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Localisation course content...')
        
        try:
            course = Course.objects.get(slug='snt-localisation-cartographie')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Localisation not found'))
            return
        
        course.chapters.all().delete()
        
        # Chapter 1: Le système GPS
        chapter1 = Chapter.objects.create(
            course=course,
            title="Le système GPS et la géolocalisation",
            description="Comprendre le fonctionnement du GPS",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Comment fonctionne le GPS?",
            content_markdown="""## GPS: Global Positioning System

### Historique
- **1973**: Développé par l'armée américaine
- **1995**: Ouvert au grand public
- **Aujourd'hui**: 5 milliards d'utilisateurs

### Le système en chiffres
- 🛰️ **31 satellites** en orbite à 20 000 km
- ⏱️ Chaque satellite fait **2 tours/jour**
- 📡 Signal radio à la vitesse de la lumière
- 📍 Précision: **5-10 mètres**

## Principe de la triangulation

Pour connaître ta position, le GPS utilise **au moins 4 satellites**:

### Étape 1: Mesure du temps
- Le satellite envoie un signal avec son heure exacte
- Ton téléphone reçoit le signal et calcule le délai
- **Distance = vitesse de la lumière × temps**

### Étape 2: Triangulation
- **1 satellite**: Tu es sur une sphère autour du satellite
- **2 satellites**: Tu es sur un cercle (intersection de 2 sphères)
- **3 satellites**: Tu es à 2 points possibles
- **4 satellites**: Position exacte + altitude!

### Coordonnées GPS
Format: **latitude, longitude**

Exemples:
| Lieu | Latitude | Longitude |
|------|----------|-----------|
| Tour Eiffel | 48.858° N | 2.294° E |
| New York | 40.712° N | 74.005° W |
| Pôle Nord | 90° N | 0° |
| Équateur | 0° | variable |

### Autres systèmes
- 🇪🇺 **Galileo** (Europe): 30 satellites
- 🇷🇺 **GLONASS** (Russie): 24 satellites
- 🇨🇳 **BeiDou** (Chine): 35 satellites""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Exemple Python: Calculer une distance GPS",
            content_markdown="""import math

# Calcule la distance entre deux points GPS en km
def distance_gps(lat1, lon1, lat2, lon2):
    # Rayon de la Terre en km
    R = 6371
    
    # Conversion en radians
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    # Formule de Haversine
    a = math.sin(delta_lat/2)**2 + \
        math.cos(lat1_rad) * math.cos(lat2_rad) * \
        math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

# Exemples de distances
print("=== DISTANCES GPS ===\\n")

# Paris -> Lyon
paris = (48.8566, 2.3522)
lyon = (45.7640, 4.8357)
d = distance_gps(*paris, *lyon)
print(f"Paris → Lyon: {d:.1f} km")

# Tour Eiffel -> Arc de Triomphe
eiffel = (48.8584, 2.2945)
arc = (48.8738, 2.2950)
d = distance_gps(*eiffel, *arc)
print(f"Tour Eiffel → Arc de Triomphe: {d:.2f} km")

# New York -> Los Angeles
ny = (40.7128, -74.0060)
la = (34.0522, -118.2437)
d = distance_gps(*ny, *la)
print(f"New York → Los Angeles: {d:.0f} km")

# Paris -> Tokyo
tokyo = (35.6762, 139.6503)
d = distance_gps(*paris, *tokyo)
print(f"Paris → Tokyo: {d:.0f} km")

# Calcul du temps de trajet
print("\\n=== TEMPS DE TRAJET ===")
distance_km = distance_gps(*paris, *lyon)
vitesses = {
    "À pied (5 km/h)": 5,
    "Vélo (20 km/h)": 20,
    "Voiture (90 km/h)": 90,
    "TGV (300 km/h)": 300,
    "Avion (800 km/h)": 800
}

for mode, vitesse in vitesses.items():
    heures = distance_km / vitesse
    print(f"{mode:20}: {heures:.1f}h")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='EXERCISE',
            title="Exercice: Calculateur d'itinéraire",
            content_markdown="""Crée un programme qui calcule un itinéraire entre plusieurs villes.

**Fonctionnalités:**
1. Liste de villes avec coordonnées GPS
2. Calcul de distance entre 2 villes
3. Calcul d'un trajet multi-étapes
4. Estimation du temps selon le mode de transport

**Exemple:**
```python
villes = {
    "Paris": (48.8566, 2.3522),
    "Lyon": (45.7640, 4.8357),
    "Marseille": (43.2965, 5.3698),
    "Bordeaux": (44.8378, -0.5792)
}

# Itinéraire: Paris → Lyon → Marseille
trajet = ["Paris", "Lyon", "Marseille"]
```

**Résultat attendu:**
```
ITINÉRAIRE
==========
Paris → Lyon: 392 km
Lyon → Marseille: 278 km

TOTAL: 670 km

EN VOITURE (90 km/h): 7.4 heures
EN TRAIN (200 km/h): 3.4 heures
```""",
            order=3
        )
        
        # Chapter 2: La cartographie numérique
        chapter2 = Chapter.objects.create(
            course=course,
            title="Cartographie et services de géolocalisation",
            description="Comment fonctionnent Google Maps et OpenStreetMap",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les services de cartographie",
            content_markdown="""## Google Maps vs OpenStreetMap

### Google Maps (2005)
- 🏢 **Propriétaire**: Google (privé)
- 💰 **Modèle**: Gratuit avec publicités
- 📸 **Données**: Photos satellites, Street View
- 🚗 **Voitures**: 200+ pour Street View
- 🌍 **Couverture**: 220 pays
- ⚡ **Mise à jour**: Automatique par algorithmes
- ❌ **Limites**: Données non libres

### OpenStreetMap (2004)
- 👥 **Propriétaire**: Communauté (open source)
- 💚 **Modèle**: Complètement gratuit
- ✏️ **Données**: Contributeurs bénévoles
- 🌐 **Couverture**: Monde entier
- 🔄 **Mise à jour**: Par les utilisateurs
- ✅ **Avantages**: Données libres, modifiables

## Comment ça marche?

### Les tuiles de carte
Les cartes en ligne utilisent des **tuiles** (tiles):
- Images carrées de 256×256 pixels
- Organisées en niveaux de zoom (0 à 20)
- **Zoom 0**: Le monde entier en 1 tuile
- **Zoom 20**: Précision de 10 cm

### Calcul du nombre de tuiles
- Zoom 1: 2² = 4 tuiles
- Zoom 5: 2¹⁰ = 1 024 tuiles
- Zoom 10: 2²⁰ = ~1 million de tuiles
- Zoom 20: 2⁴⁰ = **1 trillion de tuiles!**

### Calcul d'itinéraire
**Algorithme de Dijkstra:**
1. Modélise les routes comme un graphe
2. Trouve le chemin le plus court
3. Tient compte du trafic en temps réel
4. Propose des alternatives

**Sources de données:**
- 📍 Position GPS de millions de téléphones
- 🚗 Capteurs sur les routes
- 📱 Applications de navigation (Waze...)
- 🤖 Intelligence artificielle

## Applications populaires

| App | Utilisateurs | Spécialité |
|-----|--------------|------------|
| Google Maps | 1 milliard | Tout-en-un |
| Waze | 150 millions | Trafic temps réel |
| Citymapper | 50 millions | Transports publics |
| Komoot | 30 millions | Randonnée/vélo |
| Pokémon GO | 600 millions | Jeu en réalité augmentée |""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz: Cartographie numérique",
            content_markdown="""**Question 1:** Quelle est la différence principale entre Google Maps et OpenStreetMap?
- a) La qualité des cartes
- b) OpenStreetMap est open source et communautaire ✓
- c) Google Maps est plus ancien
- d) Il n'y a pas de différence

**Question 2:** Qu'est-ce qu'une "tuile" de carte?
- a) Une ville sur la carte
- b) Un pays
- c) Une image carrée 256×256 pixels ✓
- d) Un satellite GPS

**Question 3:** Comment Google Maps calcule-t-il le trafic?
- a) Avec des caméras
- b) En analysant les positions GPS des téléphones ✓
- c) Avec des hélicoptères
- d) C'est aléatoire

**Question 4:** Combien de tuiles au zoom 10?
- a) 100
- b) 1 024
- c) ~1 million ✓
- d) 1 milliard""",
            order=2
        )
        
        # Chapter 3: Vie privée et géolocalisation
        chapter3 = Chapter.objects.create(
            course=course,
            title="Géolocalisation et vie privée",
            description="Enjeux de confidentialité et protection des données",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les dangers de la géolocalisation",
            content_markdown="""## Pourquoi c'est sensible?

### Ce que révèle ta position:
- 🏠 **Ton domicile**: où tu habites
- 🏫 **Ton école/travail**: où tu vas chaque jour
- 🏥 **Tes lieux de soin**: médecins, hôpitaux
- 🙏 **Tes lieux de culte**: religion
- 🎉 **Tes habitudes**: bars, restaurants, amis
- 💑 **Ta vie privée**: relations, rencontres

### Exemples de problèmes

**Cas 1: Strava et bases militaires (2018)**
- Application de course à pied
- Publiait une carte mondiale des trajets
- Révélait l'emplacement de bases militaires secrètes!
- Soldats qui couraient avec l'app

**Cas 2: Les métadonnées photos**
- Chaque photo contient des données EXIF
- Inclut: date, heure, modèle d'appareil, **GPS**
- Publier une photo = révéler où tu étais

**Cas 3: Le stalking**
- Harcèlement par géolocalisation
- Applications "Find My Friends" mal utilisées
- Conjoints jaloux, ex-partenaires...

## Les risques

### Pour les individus
- 🔍 **Surveillance**: Être suivi en permanence
- 🎯 **Publicité ciblée**: Géo-marketing
- 💰 **Vol**: Cambrioleurs savent quand tu es absent
- 👤 **Harcèlement**: Suivre quelqu'un physiquement

### Pour les entreprises
- 🏢 **Espionnage industriel**: Savoir qui va où
- 📊 **Analyse de comportement**: Études de marché
- 💳 **Discrimination tarifaire**: Prix selon le quartier

## RGPD et protection

### Droits en Europe
- ✅ **Consentement explicite** requis
- ✅ **Droit à l'oubli**: Supprimer ses données
- ✅ **Transparence**: Savoir qui a tes données
- ✅ **Portabilité**: Récupérer ses données
- ⚖️ **Amendes**: Jusqu'à 4% du chiffre d'affaires

### Bonnes pratiques
1. ⚙️ **Désactive** la géolocalisation par défaut
2. 📱 Autorise **seulement pendant l'utilisation**
3. 🗑️ Supprime l'historique régulièrement
4. 📸 Retire les métadonnées avant de partager
5. 🔒 Utilise un VPN si nécessaire
6. 👤 Ne partage pas ta position sur les réseaux sociaux""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Exemple: Analyser les métadonnées d'une photo",
            content_markdown="""# Simulation d'analyse de métadonnées EXIF

def analyser_exif(photo_data):
    # Données EXIF typiques d'une photo
    print("=== MÉTADONNÉES EXIF ===\\n")
    
    for cle, valeur in photo_data.items():
        if cle == "GPS":
            lat, lon = valeur
            print(f"⚠️ GPS: {lat}° N, {lon}° E")
            print(f"   → Localisation précise révélée!")
        else:
            print(f"{cle}: {valeur}")
    
    # Vérification des risques
    print("\\n=== ANALYSE DE RISQUES ===")
    risques = []
    
    if "GPS" in photo_data:
        risques.append("🔴 Position GPS exposée")
    if "Date" in photo_data:
        risques.append("🟡 Date et heure visibles")
    if "Appareil" in photo_data:
        risques.append("🟢 Modèle d'appareil connu")
    
    for risque in risques:
        print(risque)
    
    # Recommandation
    print("\\n💡 RECOMMANDATION:")
    if "GPS" in photo_data:
        print("   Supprimez les données GPS avant publication!")
    else:
        print("   Métadonnées GPS absentes ✓")

# Exemple 1: Photo avec GPS
photo1 = {
    "Nom": "vacances_plage.jpg",
    "Date": "2024-08-15 14:32:05",
    "Appareil": "iPhone 15 Pro",
    "Résolution": "4032x3024",
    "GPS": (43.2965, 5.3698)  # Marseille
}

print("PHOTO 1: Vacances")
print("=" * 40)
analyser_exif(photo1)

# Exemple 2: Photo sans GPS
photo2 = {
    "Nom": "sunset.jpg",
    "Date": "2024-08-16 20:15:42",
    "Appareil": "Canon EOS R5",
    "Résolution": "8192x5464"
}

print("\\n\\nPHOTO 2: Coucher de soleil")
print("=" * 40)
analyser_exif(photo2)

# Fonction pour nettoyer les métadonnées
def nettoyer_exif(photo_data):
    donnees_propres = photo_data.copy()
    if "GPS" in donnees_propres:
        del donnees_propres["GPS"]
        print("✓ Données GPS supprimées")
    return donnees_propres

print("\\n\\n=== NETTOYAGE ===")
photo1_propre = nettoyer_exif(photo1)
print(f"Avant: {len(photo1)} métadonnées")
print(f"Après: {len(photo1_propre)} métadonnées")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Projet: Audit de confidentialité",
            content_markdown="""Crée un programme d'audit de confidentialité pour applications.

**Fonctionnalités:**
1. Liste d'applications avec leurs permissions
2. Analyse des risques par type de permission
3. Score de confidentialité (0-100)
4. Recommandations personnalisées

**Permissions à analyser:**
- GPS (localisation)
- Caméra
- Microphone
- Contacts
- Photos
- Calendrier

**Exemple de sortie:**
```
AUDIT DE CONFIDENTIALITÉ
========================

Application: Instagram
Permissions accordées:
  ✓ Localisation (toujours)      [🔴 Risque élevé]
  ✓ Appareil photo                [🟢 Normal]
  ✓ Contacts                      [🟡 Risque moyen]
  ✓ Microphone                    [🟢 Normal]

SCORE: 65/100

RECOMMANDATIONS:
• Passe la localisation en "Pendant l'utilisation"
• Révoque l'accès aux contacts si inutile
• Désactive les publicités géolocalisées

Application: WhatsApp
[...]
```

**Bonus:** Calcule un score global pour toutes les apps!""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
