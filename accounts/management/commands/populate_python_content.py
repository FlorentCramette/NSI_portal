"""
Management command to populate SNT Python course with interactive content
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate SNT Python course with interactive content'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('📚 Création du contenu interactif pour SNT Python...'))

        # Get the course
        try:
            course = Course.objects.get(slug='snt-python-debutant')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('❌ Cours SNT Python non trouvé'))
            return

        # Chapter 1: Variables et Types
        chapter1, created = Chapter.objects.get_or_create(
            course=course,
            slug='variables-et-types',
            defaults={
                'title': 'Variables et Types de Données',
                'description': 'Découvrez les variables, les types de données et les opérations de base en Python',
                'order': 1,
                'is_published': True,
            }
        )

        if created:
            # Block 1: Introduction
            ContentBlock.objects.create(
                chapter=chapter1,
                type='TEXT',
                title='Qu\'est-ce qu\'une variable?',
                content_markdown='''
<p>Une <strong>variable</strong> est comme une boîte qui contient une valeur. En Python, on crée une variable en lui donnant un nom et une valeur.</p>

<p>Par exemple:</p>
<ul>
    <li><code>age = 15</code> - crée une variable "age" qui contient le nombre 15</li>
    <li><code>prenom = "Alice"</code> - crée une variable "prenom" qui contient le texte "Alice"</li>
</ul>

<p>Les règles pour nommer une variable:</p>
<ul>
    <li>Pas d'espaces (utilisez _ à la place)</li>
    <li>Commence par une lettre ou _</li>
    <li>Évitez les accents</li>
</ul>
''',
                order=1
            )

            # Block 2: Interactive Code - Variables
            ContentBlock.objects.create(
                chapter=chapter1,
                type='CODE_SAMPLE',
                title='💻 Essayez vous-même!',
                content_markdown='''# Créer des variables
prenom = "Alice"
age = 15
taille = 1.65

# Afficher les variables
print("Prénom:", prenom)
print("Age:", age)
print("Taille:", taille, "m")

# Calculer avec des variables
annee_naissance = 2025 - age
print("Année de naissance:", annee_naissance)''',
                order=2
            )

            # Block 3: Types de données
            ContentBlock.objects.create(
                chapter=chapter1,
                type='TEXT',
                title='Les types de données',
                content_markdown='''
<p>Python comprend plusieurs <strong>types de données</strong>:</p>

<table class="min-w-full border border-gray-300">
    <thead class="bg-gray-100">
        <tr>
            <th class="border border-gray-300 px-4 py-2">Type</th>
            <th class="border border-gray-300 px-4 py-2">Exemple</th>
            <th class="border border-gray-300 px-4 py-2">Utilisation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>int</code></td>
            <td class="border border-gray-300 px-4 py-2"><code>42</code></td>
            <td class="border border-gray-300 px-4 py-2">Nombres entiers</td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>float</code></td>
            <td class="border border-gray-300 px-4 py-2"><code>3.14</code></td>
            <td class="border border-gray-300 px-4 py-2">Nombres décimaux</td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>str</code></td>
            <td class="border border-gray-300 px-4 py-2"><code>"Bonjour"</code></td>
            <td class="border border-gray-300 px-4 py-2">Texte (chaînes de caractères)</td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>bool</code></td>
            <td class="border border-gray-300 px-4 py-2"><code>True / False</code></td>
            <td class="border border-gray-300 px-4 py-2">Valeurs logiques</td>
        </tr>
    </tbody>
</table>

<p class="mt-4">Utilisez la fonction <code>type()</code> pour connaître le type d'une variable!</p>
''',
                order=3
            )

            # Block 4: Interactive Code - Types
            ContentBlock.objects.create(
                chapter=chapter1,
                type='CODE_SAMPLE',
                title='💻 Découvrez les types',
                content_markdown='''# Créer différents types de variables
nombre_entier = 42
nombre_decimal = 3.14
texte = "Python"
vrai_ou_faux = True

# Afficher le type de chaque variable
print("Type de nombre_entier:", type(nombre_entier))
print("Type de nombre_decimal:", type(nombre_decimal))
print("Type de texte:", type(texte))
print("Type de vrai_ou_faux:", type(vrai_ou_faux))

# Conversion de types
age_texte = "15"
age_nombre = int(age_texte)  # Convertir en nombre
print("Age converti:", age_nombre)
print("Type:", type(age_nombre))''',
                order=4
            )

            # Block 5: Exercise
            ContentBlock.objects.create(
                chapter=chapter1,
                type='EXERCISE',
                title='✏️ Exercice: Créez votre carte d\'identité',
                content_markdown='''
<p>Créez un programme qui affiche votre carte d'identité virtuelle avec:</p>
<ul>
    <li>Votre prénom et nom</li>
    <li>Votre âge</li>
    <li>Votre ville</li>
    <li>Votre classe</li>
</ul>

<p><strong>Exemple de résultat attendu:</strong></p>
<pre>
=== CARTE D'IDENTITÉ ===
Prénom: Alice
Nom: MARTIN
Age: 15 ans
Ville: Paris
Classe: Seconde 3
</pre>

<p><em>Astuce: Utilisez <code>print()</code> et créez une variable pour chaque information!</em></p>
''',
                order=5
            )

            self.stdout.write(self.style.SUCCESS(f'  ✓ Chapitre "{chapter1.title}" créé avec {chapter1.content_blocks.count()} blocs'))

        # Chapter 2: Conditions
        chapter2, created = Chapter.objects.get_or_create(
            course=course,
            slug='conditions-if-else',
            defaults={
                'title': 'Les Conditions (if, else)',
                'description': 'Apprenez à prendre des décisions dans vos programmes',
                'order': 2,
                'is_published': True,
            }
        )

        if created:
            # Block 1: Introduction aux conditions
            ContentBlock.objects.create(
                chapter=chapter2,
                type='TEXT',
                title='Prendre des décisions',
                content_markdown='''
<p>Les <strong>conditions</strong> permettent à votre programme de prendre des décisions. C'est comme dans la vraie vie:</p>

<ul>
    <li><strong>Si</strong> il pleut, alors je prends un parapluie</li>
    <li><strong>Sinon</strong>, je n'en prends pas</li>
</ul>

<p>En Python, on utilise <code>if</code> (si) et <code>else</code> (sinon):</p>

<pre><code>if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")</code></pre>

<p><em>Important: remarquez l'indentation (les espaces) avant les lignes après <code>if</code> et <code>else</code>!</em></p>
''',
                order=1
            )

            # Block 2: Interactive Code - Conditions simples
            ContentBlock.objects.create(
                chapter=chapter2,
                type='CODE_SAMPLE',
                title='💻 Testez les conditions',
                content_markdown='''# Exemple 1: Test d'âge
age = 16

if age >= 18:
    print("✅ Tu peux voter!")
else:
    print("❌ Tu ne peux pas encore voter")

# Exemple 2: Test de note
note = 15

if note >= 10:
    print("👍 Réussi!")
else:
    print("👎 Raté")

# Exemple 3: Comparaison de nombres
a = 10
b = 20

if a > b:
    print(a, "est plus grand que", b)
else:
    print(a, "est plus petit que", b)''',
                order=2
            )

            # Block 3: Les opérateurs de comparaison
            ContentBlock.objects.create(
                chapter=chapter2,
                type='QUIZ',
                title='Les opérateurs de comparaison',
                content_markdown='''
<table class="min-w-full border border-gray-300">
    <thead class="bg-yellow-100">
        <tr>
            <th class="border border-gray-300 px-4 py-2">Opérateur</th>
            <th class="border border-gray-300 px-4 py-2">Signification</th>
            <th class="border border-gray-300 px-4 py-2">Exemple</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>==</code></td>
            <td class="border border-gray-300 px-4 py-2">Est égal à</td>
            <td class="border border-gray-300 px-4 py-2"><code>age == 15</code></td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>!=</code></td>
            <td class="border border-gray-300 px-4 py-2">Est différent de</td>
            <td class="border border-gray-300 px-4 py-2"><code>nom != "Alice"</code></td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>&gt;</code></td>
            <td class="border border-gray-300 px-4 py-2">Est supérieur à</td>
            <td class="border border-gray-300 px-4 py-2"><code>note &gt; 10</code></td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>&lt;</code></td>
            <td class="border border-gray-300 px-4 py-2">Est inférieur à</td>
            <td class="border border-gray-300 px-4 py-2"><code>age &lt; 18</code></td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>&gt;=</code></td>
            <td class="border border-gray-300 px-4 py-2">Est supérieur ou égal à</td>
            <td class="border border-gray-300 px-4 py-2"><code>note &gt;= 10</code></td>
        </tr>
        <tr>
            <td class="border border-gray-300 px-4 py-2"><code>&lt;=</code></td>
            <td class="border border-gray-300 px-4 py-2">Est inférieur ou égal à</td>
            <td class="border border-gray-300 px-4 py-2"><code>age &lt;= 18</code></td>
        </tr>
    </tbody>
</table>
''',
                order=3
            )

            self.stdout.write(self.style.SUCCESS(f'  ✓ Chapitre "{chapter2.title}" créé avec {chapter2.content_blocks.count()} blocs'))

        self.stdout.write(self.style.SUCCESS('\n✅ Contenu interactif créé avec succès!'))
