from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Web course with interactive content'

    def handle(self, *args, **options):
        self.stdout.write('Creating SNT Web course content...')
        
        # Get the course
        try:
            course = Course.objects.get(slug='snt-web')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course SNT Web not found'))
            return
        
        # Clear existing chapters
        course.chapters.all().delete()
        
        # Chapter 1: HTML - Structure du Web
        chapter1 = Chapter.objects.create(
            course=course,
            title="HTML - La structure des pages web",
            description="Apprendre à créer la structure d'une page web avec HTML",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Qu'est-ce que le HTML?",
            content_markdown="""**HTML** (HyperText Markup Language) est le langage qui permet de créer la structure d'une page web.

## Les balises HTML

Le HTML utilise des **balises** (tags) pour définir les différents éléments d'une page:

```html
<balise>Contenu</balise>
```

### Balises principales:
- `<html>`: Racine du document
- `<head>`: En-tête (métadonnées, titre)
- `<body>`: Corps du document (contenu visible)
- `<h1>` à `<h6>`: Titres de différents niveaux
- `<p>`: Paragraphe
- `<a>`: Lien hypertexte
- `<img>`: Image""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Exemple: Structure HTML de base",
            content_markdown="""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ma première page</title>
</head>
<body>
    <h1>Bienvenue sur ma page</h1>
    <p>Ceci est mon <strong>premier paragraphe</strong> en HTML.</p>
    
    <h2>Une liste</h2>
    <ul>
        <li>Élément 1</li>
        <li>Élément 2</li>
        <li>Élément 3</li>
    </ul>
    
    <a href="https://www.example.com">Visitez ce site</a>
</body>
</html>""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='EXERCISE',
            title="Exercice: Créer une page HTML",
            content_markdown="""Crée une page HTML qui contient:
- Un titre principal (h1) avec ton prénom
- Un paragraphe de présentation
- Une liste à puces avec 3 de tes hobbies
- Un lien vers ton site web préféré

**Structure attendue:**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>...</title>
</head>
<body>
    <!-- Ton code ici -->
</body>
</html>
```""",
            order=3
        )
        
        # Chapter 2: CSS - Le style du Web
        chapter2 = Chapter.objects.create(
            course=course,
            title="CSS - Styliser les pages web",
            description="Apprendre à donner du style aux pages avec CSS",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Qu'est-ce que le CSS?",
            content_markdown="""**CSS** (Cascading Style Sheets) est le langage qui permet de mettre en forme les pages web.

## Syntaxe CSS

```css
selecteur {
    propriété: valeur;
}
```

### Exemple:
```css
h1 {
    color: blue;
    font-size: 32px;
}

p {
    color: #333;
    line-height: 1.6;
}
```

## Méthodes d'intégration

1. **Inline** (dans la balise): `<p style="color: red;">Texte</p>`
2. **Interne** (dans `<style>` dans le `<head>`)
3. **Externe** (fichier `.css` séparé) ← **Meilleure pratique**""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exemple: HTML avec CSS",
            content_markdown="""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Page avec CSS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Ma page stylisée</h1>
    <div class="card">
        <p>Ce texte est dans une <span class="highlight">carte</span> avec du style!</p>
    </div>
</body>
</html>""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz: HTML et CSS",
            content_markdown="""**Question 1:** Que signifie CSS?
- a) Computer Style System
- b) Cascading Style Sheets ✓
- c) Creative Style Solution
- d) Code Style Standard

**Question 2:** Quelle est la meilleure méthode pour intégrer du CSS?
- a) Inline dans les balises
- b) Dans une balise <style> dans le <head>
- c) Dans un fichier .css externe ✓
- d) Dans le fichier JavaScript

**Question 3:** Comment change-t-on la couleur du texte en CSS?
- a) text-color: red;
- b) font-color: red;
- c) color: red; ✓
- d) text: red;""",
            order=3
        )
        
        # Chapter 3: JavaScript - Interactivité
        chapter3 = Chapter.objects.create(
            course=course,
            title="JavaScript - Rendre les pages interactives",
            description="Introduction à JavaScript pour l'interactivité web",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Qu'est-ce que JavaScript?",
            content_markdown="""**JavaScript** est le langage de programmation du Web qui permet de rendre les pages interactives.

## Les 3 piliers du Web:
- **HTML**: Structure (le squelette)
- **CSS**: Présentation (l'apparence)
- **JavaScript**: Comportement (l'interactivité)

## Que peut faire JavaScript?

- Réagir aux actions de l'utilisateur (clics, survol, saisie...)
- Modifier le contenu d'une page dynamiquement
- Valider des formulaires
- Créer des animations
- Communiquer avec des serveurs (AJAX)
- Et bien plus!""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Exemple: Bouton interactif avec JavaScript",
            content_markdown="""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>JavaScript interactif</title>
    <style>
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        
        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <h1 id="titre">Bonjour!</h1>
    <button onclick="changerTexte()">Cliquez-moi</button>
    
    <script>
        let compteur = 0;
        
        function changerTexte() {
            compteur++;
            document.getElementById('titre').textContent = 
                'Vous avez cliqué ' + compteur + ' fois!';
        }
    </script>
</body>
</html>""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Exercice: Créer un changeur de couleur",
            content_markdown="""Crée une page HTML avec un bouton qui change la couleur de fond de la page à chaque clic.

**Objectifs:**
- Un titre "Changeur de couleur"
- Un bouton "Changer la couleur"
- Au clic, la couleur de fond change aléatoirement

**Indice JavaScript:**
```javascript
function couleurAleatoire() {
    const couleurs = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#6c5ce7'];
    const index = Math.floor(Math.random() * couleurs.length);
    return couleurs[index];
}

function changerCouleur() {
    document.body.style.backgroundColor = couleurAleatoire();
}
```""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {course.chapters.count()} chapters with {ContentBlock.objects.filter(chapter__course=course).count()} content blocks'))
