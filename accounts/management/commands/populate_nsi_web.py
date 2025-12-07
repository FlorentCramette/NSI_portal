from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI Le Web course content'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating NSI Le Web content...")
        
        course = Course.objects.get(slug='nsi-1-web')
        course.chapters.all().delete()
        
        # Chapter 1: HTML et Structure du Web
        chapter1 = Chapter.objects.create(
            course=course,
            title="HTML et Structure du Web",
            description="Decouverte du langage HTML et de la structure des pages web",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Le langage HTML",
            content_markdown="""# Le langage HTML

## Qu'est-ce que HTML ?

**HTML** (HyperText Markup Language) est le langage de balisage standard pour creer des pages web. Il definit la **structure** et le **contenu** des pages.

## Structure de base

Toute page HTML suit cette structure :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ma page</title>
</head>
<body>
    <h1>Titre principal</h1>
    <p>Un paragraphe de texte.</p>
</body>
</html>
```

## Les balises HTML

Les balises definissent les elements de la page :

- **Balises de titre** : `<h1>` a `<h6>` (du plus grand au plus petit)
- **Paragraphe** : `<p>`
- **Lien** : `<a href="url">texte</a>`
- **Image** : `<img src="url" alt="description">`
- **Listes** : `<ul>` (non ordonnee), `<ol>` (ordonnee), `<li>` (element)
- **Conteneurs** : `<div>` (bloc), `<span>` (en ligne)

## Balises semantiques

HTML5 introduit des balises semantiques qui donnent du sens au contenu :

- `<header>` : En-tete de page ou de section
- `<nav>` : Menu de navigation
- `<main>` : Contenu principal
- `<article>` : Article ou contenu independant
- `<section>` : Section de contenu
- `<footer>` : Pied de page

Ces balises ameliorent l'**accessibilite** et le **referencement SEO**.

## Attributs HTML

Les balises peuvent avoir des attributs :

```html
<a href="https://example.com" target="_blank" title="Visite le site">Lien</a>
<img src="photo.jpg" alt="Description" width="300" height="200">
<div id="header" class="container">...</div>
```

- **id** : Identifiant unique
- **class** : Classe CSS (peut etre partagee)
- **href** : URL de destination (liens)
- **src** : Source de l'image/script
- **alt** : Texte alternatif (accessibilite)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Creer une page HTML complete",
            content_markdown="""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Portfolio</title>
</head>
<body>
    <header>
        <h1>Bienvenue sur mon portfolio</h1>
        <nav>
            <ul>
                <li><a href="#about">A propos</a></li>
                <li><a href="#projects">Projets</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="about">
            <h2>A propos de moi</h2>
            <p>Je suis un etudiant passionne par l'informatique.</p>
            <img src="photo.jpg" alt="Ma photo" width="200">
        </section>
        
        <section id="projects">
            <h2>Mes projets</h2>
            <article>
                <h3>Projet 1 : Site web de recettes</h3>
                <p>Un site pour partager des recettes de cuisine.</p>
                <a href="projet1.html">Voir le projet</a>
            </article>
        </section>
        
        <section id="contact">
            <h2>Contact</h2>
            <form>
                <label for="name">Nom :</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email :</label>
                <input type="email" id="email" name="email" required>
                
                <button type="submit">Envoyer</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>2024 Mon Portfolio. Tous droits reserves.</p>
    </footer>
</body>
</html>""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz : HTML et structure",
            content_markdown="""**Question 1:** Que signifie HTML ?
- a) HyperText Markup Language ✓
- b) High Tech Modern Language
- c) Home Tool Markup Language
- d) Hyperlink and Text Markup Language

**Question 2:** Quelle balise definit le contenu principal d'une page ?
- a) `<body>`
- b) `<main>` ✓
- c) `<content>`
- d) `<principal>`

**Question 3:** Quelle est la syntaxe correcte pour un lien hypertexte ?
- a) `<link href="url">texte</link>`
- b) `<a url="page">texte</a>`
- c) `<a href="url">texte</a>` ✓
- d) `<href="url">texte</href>`

**Question 4:** A quoi sert l'attribut "alt" d'une image ?
- a) A definir la largeur de l'image
- b) A fournir un texte alternatif pour l'accessibilite ✓
- c) A modifier la couleur de l'image
- d) A creer un lien sur l'image""",
            order=3
        )
        
        # Chapter 2: CSS et Mise en Forme
        chapter2 = Chapter.objects.create(
            course=course,
            title="CSS et Mise en Forme",
            description="Apprendre a styliser les pages web avec CSS",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les bases du CSS",
            content_markdown="""# CSS : Cascading Style Sheets

## Qu'est-ce que le CSS ?

**CSS** (Cascading Style Sheets) est le langage utilise pour **styliser** les pages HTML. Il permet de controler :
- Les **couleurs** et **polices**
- La **disposition** et le **positionnement**
- Les **tailles** et **espacements**
- Les **animations** et **transitions**

## Trois facons d'utiliser CSS

### 1. CSS en ligne (inline)
```html
<p style="color: blue; font-size: 16px;">Texte bleu</p>
```

### 2. CSS interne (dans head)
```html
<style>
    p { color: blue; font-size: 16px; }
</style>
```

### 3. CSS externe (fichier separe) - Recommande
```html
<link rel="stylesheet" href="style.css">
```

## Selecteurs CSS

Les selecteurs permettent de cibler les elements HTML :

```css
/* Selecteur de balise */
h1 { color: red; }

/* Selecteur de classe */
.container { width: 80%; margin: 0 auto; }

/* Selecteur d'ID */
#header { background-color: navy; }

/* Selecteur descendant */
nav a { text-decoration: none; }

/* Pseudo-classe */
a:hover { color: orange; }
```

## Proprietes CSS courantes

### Couleurs et texte
```css
color: #3498db;
background-color: #ecf0f1;
font-size: 18px;
font-family: Arial, sans-serif;
text-align: center;
font-weight: bold;
```

### Box Model
```css
width: 300px;
height: 200px;
padding: 20px;
margin: 10px;
border: 2px solid black;
```

## Le modele de boite (Box Model)

Chaque element HTML est une boite composee de :
1. **Content** : Le contenu (texte, image)
2. **Padding** : Espacement interne
3. **Border** : La bordure
4. **Margin** : Espacement externe

## Flexbox

Flexbox est un systeme de disposition moderne :

```css
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}
```""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Creer une mise en page avec CSS",
            content_markdown="""/* style.css */

/* Reset et base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Header */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

header h1 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

/* Navigation */
nav {
    background-color: #2c3e50;
    padding: 1rem 0;
}

nav ul {
    display: flex;
    justify-content: center;
    gap: 2rem;
    list-style: none;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

nav a:hover {
    background-color: #34495e;
}

/* Main content */
main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 2rem;
}

section {
    margin-bottom: 3rem;
    padding: 2rem;
    background-color: #f8f9fa;
    border-radius: 10px;
}

/* Cards */
article {
    flex: 1;
    min-width: 300px;
    padding: 1.5rem;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

article:hover {
    transform: translateY(-5px);
}

/* Responsive */
@media (max-width: 768px) {
    nav ul {
        flex-direction: column;
        gap: 0.5rem;
    }
}""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz : CSS",
            content_markdown="""**Question 1:** Quelle est la methode recommandee pour inclure du CSS ?
- a) CSS en ligne (inline)
- b) CSS interne (dans head)
- c) CSS externe (fichier separe) ✓
- d) JavaScript

**Question 2:** Que signifie le selecteur ".container" en CSS ?
- a) Selectionne tous les elements container
- b) Selectionne l'element avec l'ID container
- c) Selectionne les elements avec la classe container ✓
- d) Selectionne le premier container

**Question 3:** Quelle propriete CSS controle l'espacement interne d'un element ?
- a) margin
- b) padding ✓
- c) border
- d) spacing

**Question 4:** Comment centrer un element horizontalement avec Flexbox ?
- a) text-align: center
- b) align-items: center
- c) justify-content: center ✓
- d) margin: center""",
            order=3
        )
        
        # Chapter 3: Protocoles Web et Securite
        chapter3 = Chapter.objects.create(
            course=course,
            title="Protocoles Web et Securite",
            description="Comprendre HTTP, HTTPS et les enjeux de securite sur le web",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Le protocole HTTP",
            content_markdown="""# Protocoles Web

## Le protocole HTTP

**HTTP** (HyperText Transfer Protocol) est le protocole de communication du Web. Il definit comment les **clients** (navigateurs) et les **serveurs** echangent des informations.

### Fonctionnement

1. Le client envoie une **requete HTTP** au serveur
2. Le serveur traite la requete
3. Le serveur renvoie une **reponse HTTP** au client

### Methodes HTTP

- **GET** : Recuperer une ressource (page, image)
- **POST** : Envoyer des donnees au serveur (formulaire)
- **PUT** : Mettre a jour une ressource
- **DELETE** : Supprimer une ressource

### Codes de statut HTTP

- **2xx** : Succes (200 OK, 201 Created)
- **3xx** : Redirection (301 Moved Permanently)
- **4xx** : Erreur client (400 Bad Request, 404 Not Found)
- **5xx** : Erreur serveur (500 Internal Server Error)

## HTTPS : HTTP Securise

**HTTPS** = HTTP + **TLS/SSL** (chiffrement)

### Avantages de HTTPS

1. **Confidentialite** : Les donnees sont chiffrees
2. **Integrite** : Les donnees ne peuvent pas etre modifiees
3. **Authentification** : Verification de l'identite du serveur

### Certificat SSL/TLS

- Delivre par une **autorite de certification** (CA)
- Contient la cle publique du serveur
- Visible dans la barre d'adresse (cadenas)

## Cookies et Sessions

### Cookies

Petits fichiers stockes par le navigateur contenant :
- Identifiants de session
- Preferences utilisateur
- Donnees de suivi

Attributs importants :
- **Secure** : Envoye uniquement en HTTPS
- **HttpOnly** : Inaccessible en JavaScript (securite XSS)
- **SameSite** : Protection CSRF

## Securite Web

### Attaques courantes

**1. XSS (Cross-Site Scripting)**
- Injection de code JavaScript malveillant
- Protection : Echapper les donnees utilisateur

**2. CSRF (Cross-Site Request Forgery)**
- Execution d'actions non autorisees
- Protection : Token CSRF, SameSite cookies

**3. Injection SQL**
- Manipulation de requetes base de donnees
- Protection : Requetes preparees, validation

### Bonnes pratiques

- Utiliser **HTTPS** systematiquement
- Valider et echapper les **entrees utilisateur**
- Utiliser des **mots de passe forts** et le hachage
- Tenir les logiciels a jour""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Simulateur de requetes HTTP",
            content_markdown="""# Simulateur de requetes HTTP en Python
import time

# Simulation de requetes HTTP
def send_http_request(method, url, headers=None, body=None):
    # Simule l'envoi d'une requete HTTP
    print(f"\\n{'='*50}")
    print(f"REQUETE HTTP")
    print(f"{'='*50}")
    print(f"Methode: {method}")
    print(f"URL: {url}")
    
    if headers:
        print(f"\\nEn-tetes:")
        for key, value in headers.items():
            print(f"  {key}: {value}")
    
    if body:
        print(f"\\nCorps de la requete:")
        print(f"  {body}")
    
    # Simulation du temps de reponse
    time.sleep(0.3)
    
    # Simulation de la reponse
    if method == "GET" and url == "/users":
        status = 200
        response = {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
    elif method == "POST" and url == "/users":
        status = 201
        response = {"message": "Utilisateur cree", "id": 3}
    elif url == "/admin":
        status = 403
        response = {"error": "Acces refuse"}
    elif url == "/not-found":
        status = 404
        response = {"error": "Page non trouvee"}
    else:
        status = 200
        response = {"message": "OK"}
    
    print(f"\\n{'='*50}")
    print(f"REPONSE HTTP")
    print(f"{'='*50}")
    print(f"Statut: {status}")
    print(f"Reponse: {response}")
    
    return status, response

def get_status_text(code):
    statuses = {
        200: "OK", 201: "Created", 400: "Bad Request",
        401: "Unauthorized", 403: "Forbidden", 404: "Not Found",
        500: "Internal Server Error"
    }
    return statuses.get(code, "Unknown")

# Tests de differentes requetes
print("Simulation de requetes HTTP\\n")

# GET : Recuperer des utilisateurs
send_http_request(
    method="GET",
    url="/users",
    headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
)

# POST : Creer un utilisateur
send_http_request(
    method="POST",
    url="/users",
    headers={"Content-Type": "application/json"},
    body='{"name": "Charlie", "email": "charlie@example.com"}'
)

# GET : Acces refuse
send_http_request(method="GET", url="/admin")

# GET : Page non trouvee
send_http_request(method="GET", url="/not-found")

# Analyse des codes de statut
print("\\n\\nAnalyse des codes de statut HTTP:\\n")
codes = [200, 201, 301, 400, 401, 403, 404, 500, 503]
for code in codes:
    text = get_status_text(code)
    category = "Succes" if 200 <= code < 300 else \
                "Redirection" if 300 <= code < 400 else \
                "Erreur client" if 400 <= code < 500 else "Erreur serveur"
    print(f"  {code} {text:20} - {category}")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz : Protocoles et securite",
            content_markdown="""**Question 1:** Quelle est la difference principale entre HTTP et HTTPS ?
- a) HTTPS est plus rapide
- b) HTTPS chiffre les communications ✓
- c) HTTP est plus securise
- d) Aucune difference

**Question 2:** Que signifie un code de statut HTTP 404 ?
- a) Requete reussie
- b) Erreur serveur
- c) Acces refuse
- d) Ressource non trouvee ✓

**Question 3:** Quelle methode HTTP est utilisee pour recuperer une ressource ?
- a) POST
- b) GET ✓
- c) PUT
- d) DELETE

**Question 4:** Qu'est-ce qu'une attaque XSS ?
- a) Injection de code JavaScript malveillant ✓
- b) Vol de mot de passe
- c) Attaque par deni de service
- d) Chiffrement des donnees

**Question 5:** Quel attribut de cookie empeche l'acces en JavaScript ?
- a) Secure
- b) SameSite
- c) HttpOnly ✓
- d) Domain""",
            order=3
        )
        
        blocks_count = sum(ch.content_blocks.count() for ch in [chapter1, chapter2, chapter3])
        self.stdout.write(
            self.style.SUCCESS(f'Created 3 chapters with {blocks_count} blocks for NSI Le Web')
        )
