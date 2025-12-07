from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Internet course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Internet course content...')
        
        # Get the course
        try:
            course = Course.objects.get(slug='snt-internet')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Internet not found'))
            return
        
        # Clear existing chapters
        course.chapters.all().delete()
        
        # Chapter 1: Qu'est-ce qu'Internet?
        chapter1 = Chapter.objects.create(
            course=course,
            title="Qu'est-ce qu'Internet?",
            description="Découvrir les fondamentaux d'Internet et son histoire",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Introduction à Internet",
            content_markdown="""Internet est un **réseau mondial** d'ordinateurs interconnectés qui permet l'échange de données et d'informations à travers le monde.

## Histoire d'Internet

Internet est né dans les années **1960** aux États-Unis avec le projet **ARPANET**, un réseau militaire conçu pour résister à une attaque nucléaire.

### Dates clés:
- **1969**: Création d'ARPANET (4 ordinateurs connectés)
- **1989**: Invention du World Wide Web par Tim Berners-Lee
- **1991**: Ouverture d'Internet au grand public
- **2000s**: Explosion des réseaux sociaux et du mobile""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Comment fonctionne Internet?",
            content_markdown="""Internet fonctionne grâce à des **protocoles** qui permettent aux ordinateurs de communiquer entre eux.

## Les protocoles principaux

### TCP/IP (Transmission Control Protocol / Internet Protocol)
C'est le "langage" de base d'Internet qui permet d'envoyer et recevoir des données en les découpant en petits paquets.

### HTTP/HTTPS (HyperText Transfer Protocol)
Protocole utilisé pour naviguer sur le Web. Le **S** signifie **Secure** (sécurisé).

### DNS (Domain Name System)
Système qui traduit les noms de domaine (comme `google.com`) en adresses IP (comme `142.250.179.46`).""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Les bases d'Internet",
            content_markdown="""**Question 1:** En quelle année Internet a-t-il été ouvert au grand public?
- a) 1969
- b) 1989
- c) 1991 ✓
- d) 2000

**Question 2:** Que signifie le "S" dans HTTPS?
- a) Server
- b) Secure ✓
- c) System
- d) Simple

**Question 3:** Quel protocole traduit les noms de domaine en adresses IP?
- a) HTTP
- b) TCP
- c) DNS ✓
- d) FTP""",
            order=3
        )
        
        # Chapter 2: Les adresses IP
        chapter2 = Chapter.objects.create(
            course=course,
            title="Les adresses IP et le routage",
            description="Comprendre le système d'adressage sur Internet",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Qu'est-ce qu'une adresse IP?",
            content_markdown="""Une **adresse IP** (Internet Protocol) est un identifiant unique attribué à chaque appareil connecté à Internet.

## IPv4 vs IPv6

### IPv4 (Internet Protocol version 4)
- Format: 4 nombres séparés par des points
- Exemple: `192.168.1.1`
- Limité à **4,3 milliards** d'adresses
- Épuisement des adresses disponibles

### IPv6 (Internet Protocol version 6)
- Format: 8 groupes de chiffres hexadécimaux
- Exemple: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Permet **340 sextillions** d'adresses (340 × 10³⁶)
- Solution pour l'avenir""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exemple Python: Extraire les octets d'une adresse IPv4",
            content_markdown="""# Une adresse IPv4 est composée de 4 octets (nombres entre 0 et 255)
ip_address = "192.168.1.1"

# Séparer les octets
octets = ip_address.split('.')

print(f"Adresse IP: {ip_address}")
print(f"Nombre d'octets: {len(octets)}")

for i, octet in enumerate(octets, 1):
    print(f"Octet {i}: {octet}")
    
# Vérifier la validité
valid = all(0 <= int(octet) <= 255 for octet in octets)
print(f"\\nAdresse valide: {valid}")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Valider une adresse IPv4",
            content_markdown="""Écris une fonction `is_valid_ipv4(ip)` qui retourne `True` si l'adresse IP est valide, `False` sinon.

**Critères de validité:**
- 4 octets séparés par des points
- Chaque octet est un nombre entre 0 et 255

**Exemples:**
```python
is_valid_ipv4("192.168.1.1")  # True
is_valid_ipv4("256.1.1.1")    # False (256 > 255)
is_valid_ipv4("192.168.1")    # False (seulement 3 octets)
```

**Indice:** Utilise `split('.')` et une boucle pour vérifier chaque octet.""",
            order=3
        )
        
        # Chapter 3: Le Web et les navigateurs
        chapter3 = Chapter.objects.create(
            course=course,
            title="Le Web et les navigateurs",
            description="Comprendre la différence entre Internet et le Web",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Internet vs Web",
            content_markdown="""Il est important de distinguer **Internet** et le **Web** (World Wide Web):

## Internet
- Infrastructure physique (câbles, routeurs, serveurs)
- Réseau mondial d'ordinateurs
- Permet de nombreux services: email, transfert de fichiers, messagerie instantanée, Web...

## Le Web
- Service qui fonctionne **sur** Internet
- Ensemble de pages web reliées par des liens hypertextes
- Accessible via un navigateur
- Inventé par Tim Berners-Lee en 1989

**Analogie:** Internet est comme le réseau routier, le Web est comme les voitures qui circulent dessus.""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Comment fonctionne un navigateur?",
            content_markdown="""Un **navigateur web** (Chrome, Firefox, Safari, Edge...) est un logiciel qui permet d'accéder au Web.

## Étapes de chargement d'une page:

1. **Vous tapez une URL** dans la barre d'adresse: `https://www.example.com`

2. **Résolution DNS**: Le navigateur demande l'adresse IP du serveur
   - `www.example.com` → `93.184.216.34`

3. **Requête HTTP/HTTPS**: Le navigateur envoie une demande au serveur
   - GET /index.html

4. **Réponse du serveur**: Le serveur envoie le code HTML, CSS, JavaScript

5. **Rendu de la page**: Le navigateur affiche la page web
   - Interprète le HTML
   - Applique le CSS (styles)
   - Exécute le JavaScript (interactivité)""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Internet et le Web",
            content_markdown="""**Question 1:** Quelle est la différence entre Internet et le Web?
- a) Ce sont deux mots pour la même chose
- b) Le Web est un service qui fonctionne sur Internet ✓
- c) Internet est plus récent que le Web
- d) Le Web est plus grand qu'Internet

**Question 2:** Qui a inventé le World Wide Web?
- a) Bill Gates
- b) Steve Jobs
- c) Tim Berners-Lee ✓
- d) Mark Zuckerberg

**Question 3:** Que fait le DNS?
- a) Protège contre les virus
- b) Traduit les noms de domaine en adresses IP ✓
- c) Accélère la connexion Internet
- d) Crypte les données""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
