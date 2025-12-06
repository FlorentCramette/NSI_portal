"""
Management command to create SNT (Seconde) and NSI (Première/Terminale) content
Programme conforme à l'Éducation Nationale française
"""
from django.core.management.base import BaseCommand
from courses.models import Course


class Command(BaseCommand):
    help = 'Create SNT and NSI content conforming to French national curriculum'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🎓 Création du contenu SNT et NSI...'))

        # SNT (Seconde) - 7 thématiques officielles
        self.stdout.write('\n📚 SNT - Sciences Numériques et Technologie (Seconde)')
        self.create_snt_courses()

        # NSI Première
        self.stdout.write('\n💻 NSI - Première')
        self.create_nsi_premiere_courses()

        self.stdout.write(self.style.SUCCESS('\n✅ Contenu créé avec succès!'))

    def create_snt_courses(self):
        """Create SNT courses based on official 7 themes from Education Nationale"""

        # Theme 1: Internet
        Course.objects.get_or_create(
            slug='snt-internet',
            defaults={
                'title': 'SNT - Internet',
                'level': 'SNT',
                'description': 'Comprendre le fonctionnement d\'Internet : adressage, routage, protocoles',
                'icon': '🌐',
                'image_url': 'images/courses/internet.jpg',
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Internet créé')

        # Theme 2: Web
        Course.objects.get_or_create(
            slug='snt-web',
            defaults={
                'title': 'SNT - Le Web',
                'level': 'SNT',
                'description': 'Technologies du Web : HTML, CSS, moteurs de recherche, cookies',
                'icon': '🕸️',
                'image_url': 'images/courses/web.jpg',
                'order': 2,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Web créé')

        # Theme 3: Réseaux sociaux
        Course.objects.get_or_create(
            slug='snt-reseaux-sociaux',
            defaults={
                'title': 'SNT - Réseaux Sociaux',
                'level': 'SNT',
                'description': 'Fonctionnement, modèle économique, cyberviolence, identité numérique',
                'icon': '👥',
                'image_url': 'images/courses/reseaux-sociaux.jpg',
                'order': 3,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Réseaux sociaux créé')

        # Theme 4: Données structurées
        Course.objects.get_or_create(
            slug='snt-donnees-structurees',
            defaults={
                'title': 'SNT - Données Structurées',
                'level': 'SNT',
                'description': 'Tableurs, bases de données, métadonnées, open data',
                'icon': '📊',
                'image_url': 'images/courses/donnees.jpg',
                'order': 4,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Données structurées créé')

        # Theme 5: Localisation et cartographie
        Course.objects.get_or_create(
            slug='snt-localisation-cartographie',
            defaults={
                'title': 'SNT - Localisation et Cartographie',
                'level': 'SNT',
                'description': 'GPS, géolocalisation, cartes numériques, applications',
                'icon': '📍',
                'image_url': 'images/courses/localisation.jpg',
                'order': 5,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Localisation créé')

        # Theme 6: Objets connectés
        Course.objects.get_or_create(
            slug='snt-objets-connectes',
            defaults={
                'title': 'SNT - Objets Connectés',
                'level': 'SNT',
                'description': 'Internet des objets, capteurs, actionneurs, sécurité',
                'icon': '🤖',
                'image_url': 'images/courses/objets-connectes.jpg',
                'order': 6,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Objets connectés créé')

        # Theme 7: Photographie numérique
        Course.objects.get_or_create(
            slug='snt-photo-numerique',
            defaults={
                'title': 'SNT - Photographie Numérique',
                'level': 'SNT',
                'description': 'Pixels, compression, métadonnées, traitement d\'images',
                'icon': '📷',
                'image_url': 'images/courses/photo-numerique.jpg',
                'order': 7,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Photo numérique créé')

        # SNT Bonus courses (pour préparer NSI)
        Course.objects.get_or_create(
            slug='snt-python-debutant',
            defaults={
                'title': 'SNT Bonus - Python pour Débutants',
                'level': 'SNT',
                'description': 'Initiation à la programmation Python pour préparer la NSI',
                'icon': '🐍',
                'image_url': 'images/courses/python.jpg',
                'order': 10,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Bonus Python créé')

        Course.objects.get_or_create(
            slug='snt-architecture-ordinateurs',
            defaults={
                'title': 'SNT Bonus - Architecture des Ordinateurs',
                'level': 'SNT',
                'description': 'Comprendre les composants d\'un ordinateur',
                'icon': '💻',
                'image_url': 'images/courses/architecture.jpg',
                'order': 11,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Bonus Architecture créé')

        Course.objects.get_or_create(
            slug='snt-reseaux-introduction',
            defaults={
                'title': 'SNT Bonus - Introduction aux Réseaux',
                'level': 'SNT',
                'description': 'Approfondissement sur les réseaux informatiques',
                'icon': '🔌',
                'image_url': 'images/courses/reseaux.jpg',
                'order': 12,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Bonus Réseaux créé')

        Course.objects.get_or_create(
            slug='snt-outils-collaboratifs',
            defaults={
                'title': 'SNT Bonus - Outils Collaboratifs',
                'level': 'SNT',
                'description': 'Git, GitHub, travail collaboratif en informatique',
                'icon': '🛠️',
                'image_url': 'images/courses/outils.jpg',
                'order': 13,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Bonus Outils créé')

    def create_nsi_premiere_courses(self):
        """Create NSI Première courses"""

        # 1. Programmation
        Course.objects.get_or_create(
            slug='nsi-1-programmation',
            defaults={
                'title': 'NSI 1ère - Programmation Python',
                'level': 'PREMIERE',
                'description': 'Variables, fonctions, structures de contrôle, programmation impérative',
                'icon': '🐍',
                'image_url': 'images/courses/programmation.jpg',
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Programmation créé')

        # 2. Représentation des données
        Course.objects.get_or_create(
            slug='nsi-1-representation-donnees',
            defaults={
                'title': 'NSI 1ère - Représentation des Données',
                'level': 'PREMIERE',
                'description': 'Binaire, hexadécimal, encodages, représentation des nombres, texte',
                'icon': '0️⃣',
                'image_url': 'images/courses/representation-donnees.jpg',
                'order': 2,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Représentation créé')

        # 3. Traitement de données en tables
        Course.objects.get_or_create(
            slug='nsi-1-traitement-donnees',
            defaults={
                'title': 'NSI 1ère - Traitement de Données',
                'level': 'PREMIERE',
                'description': 'CSV, JSON, recherche, tri, fusion de tables',
                'icon': '📋',
                'image_url': 'images/courses/traitement-donnees.jpg',
                'order': 3,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Traitement créé')

        # 4. Algorithmique
        Course.objects.get_or_create(
            slug='nsi-1-algorithmique',
            defaults={
                'title': 'NSI 1ère - Algorithmique',
                'level': 'PREMIERE',
                'description': 'Algorithmes de tri, recherche, complexité, preuve de correction',
                'icon': '🔍',
                'image_url': 'images/courses/algorithmique.jpg',
                'order': 4,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Algorithmique créé')

        # 5. Architecture matérielle
        Course.objects.get_or_create(
            slug='nsi-1-architecture',
            defaults={
                'title': 'NSI 1ère - Architecture Matérielle',
                'level': 'PREMIERE',
                'description': 'Processeur, mémoire, systèmes d\'exploitation, assembleur',
                'icon': '💻',
                'image_url': 'images/courses/architecture.jpg',
                'order': 5,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Architecture créé')

        # 6. Réseaux
        Course.objects.get_or_create(
            slug='nsi-1-reseaux',
            defaults={
                'title': 'NSI 1ère - Réseaux',
                'level': 'PREMIERE',
                'description': 'Modèle OSI, protocoles TCP/IP, routage, sécurité',
                'icon': '🌐',
                'image_url': 'images/courses/reseaux.jpg',
                'order': 6,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Réseaux créé')

        # 7. Web
        Course.objects.get_or_create(
            slug='nsi-1-web',
            defaults={
                'title': 'NSI 1ère - Le Web',
                'level': 'PREMIERE',
                'description': 'HTML, CSS, JavaScript, architecture client-serveur, formulaires',
                'icon': '🌐',
                'image_url': 'images/courses/web.jpg',
                'order': 7,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI 1ère Web créé')
