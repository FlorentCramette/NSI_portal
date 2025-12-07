from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Réseaux Sociaux course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Réseaux Sociaux course content...')
        
        # Get the course
        try:
            course = Course.objects.get(slug='snt-reseaux-sociaux')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Réseaux Sociaux not found'))
            return
        
        # Clear existing chapters
        course.chapters.all().delete()
        
        # Chapter 1: Introduction aux réseaux sociaux
        chapter1 = Chapter.objects.create(
            course=course,
            title="Qu'est-ce qu'un réseau social?",
            description="Découvrir les réseaux sociaux et leur impact",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Définition et histoire",
            content_markdown="""Un **réseau social** est un service en ligne qui permet aux utilisateurs de créer un profil, de partager du contenu et d'interagir avec d'autres utilisateurs.

## Histoire des réseaux sociaux

### Années 2000 - Les pionniers
- **2004**: Création de **Facebook** par Mark Zuckerberg
- **2005**: Lancement de **YouTube**
- **2006**: Naissance de **Twitter**

### Années 2010 - L'explosion mobile
- **2010**: **Instagram** révolutionne le partage de photos
- **2011**: **Snapchat** introduit les messages éphémères
- **2016**: **TikTok** devient viral avec les vidéos courtes

### Aujourd'hui
- Plus de **5 milliards** d'utilisateurs dans le monde
- En moyenne **2h30** passées par jour sur les réseaux sociaux
- Impact majeur sur la société, la politique, l'économie

## Principaux réseaux sociaux

| Réseau | Utilisateurs | Usage principal |
|--------|--------------|-----------------|
| Facebook | 3 milliards | Général, amis |
| YouTube | 2,5 milliards | Vidéos |
| Instagram | 2 milliards | Photos, stories |
| TikTok | 1,5 milliard | Vidéos courtes |
| Twitter/X | 500 millions | Actualités, débats |""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Fonctionnement d'un réseau social",
            content_markdown="""## Les éléments clés

### Le profil
- Informations personnelles (nom, photo, bio)
- Liste d'amis/abonnés/contacts
- Historique de publications

### Le fil d'actualité (feed)
- Affiche les publications des autres utilisateurs
- Trié par un **algorithme** (pas chronologique)
- Personnalisé selon vos interactions

### Les interactions
- **Like** / J'aime: Apprécier un contenu
- **Commentaire**: Réagir par du texte
- **Partage**: Diffuser à son réseau
- **Message privé**: Communication directe

### Les algorithmes
Les réseaux sociaux utilisent des algorithmes d'**Intelligence Artificielle** pour:
- Proposer du contenu personnalisé
- Maximiser le temps passé sur la plateforme
- Cibler la publicité
- Détecter les contenus inappropriés

⚠️ **Attention**: Ces algorithmes peuvent créer des "bulles de filtres" où vous ne voyez que des opinions similaires aux vôtres.""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Les réseaux sociaux",
            content_markdown="""**Question 1:** En quelle année Facebook a-t-il été créé?
- a) 2000
- b) 2004 ✓
- c) 2010
- d) 2015

**Question 2:** Qu'est-ce qu'une "bulle de filtre"?
- a) Un filtre photo
- b) Une notification
- c) Un algorithme qui ne montre que des opinions similaires ✓
- d) Une fonction de messagerie

**Question 3:** Combien de temps en moyenne passe-t-on sur les réseaux sociaux par jour?
- a) 30 minutes
- b) 1 heure
- c) 2h30 ✓
- d) 5 heures""",
            order=3
        )
        
        # Chapter 2: Données personnelles et vie privée
        chapter2 = Chapter.objects.create(
            course=course,
            title="Vie privée et données personnelles",
            description="Protéger ses données sur les réseaux sociaux",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Vos données ont de la valeur",
            content_markdown="""Sur les réseaux sociaux, vous êtes **à la fois l'utilisateur et le produit**. Vos données sont collectées et monétisées.

## Quelles données sont collectées?

### Données fournies volontairement
- Nom, âge, localisation
- Photos et vidéos
- Publications et commentaires
- Liste d'amis

### Données collectées automatiquement
- **Métadonnées**: Heure, lieu, appareil utilisé
- **Comportement**: Pages visitées, temps passé, clics
- **Géolocalisation**: Où vous êtes en temps réel
- **Cookies**: Suivi de votre navigation web

## Comment sont utilisées vos données?

### Publicité ciblée
Les annonceurs paient pour cibler précisément:
- Âge, sexe, localisation
- Centres d'intérêt
- Comportements d'achat

### Revente à des tiers
Certaines entreprises peuvent:
- Acheter vos données
- Créer votre profil détaillé
- Prédire vos comportements

## Le RGPD (Règlement Général sur la Protection des Données)

En Europe, le RGPD protège vos droits:
- ✅ **Droit d'accès**: Voir quelles données sont collectées
- ✅ **Droit de rectification**: Corriger vos données
- ✅ **Droit à l'oubli**: Supprimer vos données
- ✅ **Droit à la portabilité**: Récupérer vos données""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exemple Python: Analyser les métadonnées d'une photo",
            content_markdown="""# Les photos contiennent des métadonnées EXIF
# (date, lieu GPS, modèle d'appareil...)

from datetime import datetime

# Simulation de métadonnées EXIF d'une photo Instagram
metadata = {
    'DateTimeOriginal': '2024:12:07 14:30:25',
    'Make': 'Apple',
    'Model': 'iPhone 13',
    'GPSLatitude': 48.8566,
    'GPSLongitude': 2.3522,
    'ImageSize': '4032x3024'
}

print("=== Métadonnées de la photo ===\\n")

# Date et heure
date_str = metadata['DateTimeOriginal']
date = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
print(f"📅 Prise le: {date.strftime('%d/%m/%Y à %H:%M')}")

# Appareil
print(f"📱 Appareil: {metadata['Make']} {metadata['Model']}")

# Localisation (Paris dans cet exemple)
print(f"📍 Lieu: {metadata['GPSLatitude']}°N, {metadata['GPSLongitude']}°E")
print("   → Correspond à Paris, France")

# Résolution
print(f"🖼️ Résolution: {metadata['ImageSize']}")

print("\\n⚠️ Ces données peuvent révéler où vous habitez, travaillez, etc.")
print("💡 Conseil: Désactivez la géolocalisation sur vos photos!")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Audit de vie privée",
            content_markdown="""Crée un programme Python qui simule un audit de vie privée sur un profil de réseau social.

**Données du profil:**
```python
profil = {
    "nom_complet": True,  # Nom visible publiquement
    "date_naissance": True,  # Date de naissance publique
    "telephone": False,  # Numéro caché
    "email": True,  # Email visible
    "adresse": True,  # Adresse affichée
    "photos_geolocalisees": True,  # GPS activé sur les photos
    "amis_publics": True,  # Liste d'amis visible
    "posts_publics": 250,  # Nombre de posts publics
    "partage_localisation": True  # Localisation temps réel
}
```

**Ton programme doit:**
1. Compter le nombre d'informations publiques
2. Calculer un "score de risque" sur 10
3. Donner des recommandations

**Critères de risque:**
- Nom complet public: +1
- Date de naissance: +1
- Email visible: +1
- Adresse publique: +2 ⚠️
- Photos géolocalisées: +2 ⚠️
- Partage localisation temps réel: +3 ⚠️⚠️

**Exemple de sortie:**
```
🔒 AUDIT DE VIE PRIVÉE
━━━━━━━━━━━━━━━━━━━━━
Score de risque: 8/10 ⚠️ ÉLEVÉ

Recommandations:
❌ Masquer votre adresse (risque: cambriolage)
❌ Désactiver la géolocalisation des photos
❌ Passer en mode privé
```""",
            order=3
        )
        
        # Chapter 3: Cyberharcèlement et fake news
        chapter3 = Chapter.objects.create(
            course=course,
            title="Cyberharcèlement et désinformation",
            description="Se protéger et identifier les risques en ligne",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Le cyberharcèlement",
            content_markdown="""Le **cyberharcèlement** est un harcèlement qui se déroule sur Internet et les réseaux sociaux.

## Formes de cyberharcèlement

### Messages répétés
- Insultes, menaces, moqueries
- Messages privés ou commentaires publics
- Création de faux comptes pour harceler

### Diffusion de contenus
- Photos ou vidéos humiliantes
- Rumeurs et diffamation
- "Doxing": Publier des infos personnelles (adresse, téléphone...)

### Exclusion sociale
- Exclure quelqu'un d'un groupe
- Ignorer systématiquement
- Campagnes de boycott

## Conséquences

Pour la victime:
- 😔 Dépression, anxiété
- 📉 Chute des résultats scolaires
- 🚫 Isolement social
- ⚠️ Dans les cas graves: suicide

## Que faire?

### Si vous êtes victime:
1. **Ne pas répondre** aux provocations
2. **Faire des captures d'écran** (preuves)
3. **Bloquer** les harceleurs
4. **En parler** à un adulte de confiance
5. **Signaler** sur la plateforme
6. **Porter plainte** si nécessaire (3018 ou police)

### Si vous êtes témoin:
- Ne pas relayer les contenus
- Soutenir la victime
- Signaler le harcèlement
- En parler à un adulte

🆘 **Numéro d'urgence: 3018** (gratuit, confidentiel, spécialisé)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les fake news (infox)",
            content_markdown="""Les **fake news** (ou infox) sont de fausses informations diffusées intentionnellement.

## Comment les reconnaître?

### 1. Vérifier la source
- ✅ Site connu et fiable?
- ❌ Site inconnu avec un nom étrange?
- ✅ Auteur identifié?

### 2. Croiser les sources
- L'info est-elle reprise par plusieurs médias fiables?
- Utilisez les sites de fact-checking:
  - **Le Monde - Les Décodeurs**
  - **Libération - CheckNews**
  - **AFP Factuel**

### 3. Analyser le contenu
- Titre sensationnaliste? ("CHOQUANT!", "INCROYABLE!")
- Fautes d'orthographe?
- Pas de date ou date ancienne?
- Émotion > Faits?

### 4. Vérifier les images
- Utilisez la **recherche inversée d'images** (Google Images)
- Les photos peuvent être:
  - Sorties de leur contexte
  - Modifiées (Photoshop)
  - Issues d'un autre événement

## Pourquoi les fake news existent?

### Motivations:
- **Politique**: Influencer l'opinion
- **Financière**: Générer des clics et revenus publicitaires
- **Idéologique**: Promouvoir une cause
- **Humour**: Satire mal comprise

### Propagation virale:
- Les fake news se partagent **6 fois plus vite** que les vraies infos
- Les gens partagent sans vérifier
- Les algorithmes favorisent le contenu sensationnel

## Votre responsabilité

Avant de partager:
1. ✋ **STOP**: Ne partagez pas immédiatement
2. 🔍 **VÉRIFIEZ**: La source et le contenu
3. 🤔 **RÉFLÉCHISSEZ**: Est-ce crédible?
4. ✅ **PARTAGEZ**: Seulement si c'est vérifié""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Cybersécurité et désinformation",
            content_markdown="""**Question 1:** Que signifie "doxing"?
- a) Publier des mèmes
- b) Publier les informations personnelles de quelqu'un ✓
- c) Envoyer des messages privés
- d) Créer un faux profil

**Question 2:** Quel est le numéro d'urgence contre le cyberharcèlement?
- a) 15
- b) 17
- c) 112
- d) 3018 ✓

**Question 3:** Comment vérifier si une image est vraie?
- a) Regarder si elle est belle
- b) Utiliser la recherche inversée d'images ✓
- c) Demander à un ami
- d) Compter les likes

**Question 4:** Les fake news se propagent:
- a) Plus lentement que les vraies infos
- b) À la même vitesse
- c) 2 fois plus vite
- d) 6 fois plus vite ✓""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
