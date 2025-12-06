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
                'description': 'GPS, cartographie numérique, géolocalisation, calcul d\'itinéraire',
                'order': 5,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Localisation créé')
        
        # Theme 6: Informatique embarquée et objets connectés
        Course.objects.get_or_create(
            slug='snt-objets-connectes',
            defaults={
                'title': 'SNT - Objets Connectés',
                'level': 'SNT',
                'description': 'Capteurs, actionneurs, interface homme-machine, Internet des objets',
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
                'description': 'Images numériques, pixels, métadonnées, traitement d\'images',
                'order': 7,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours SNT Photo numérique créé')

    def create_nsi_premiere_courses(self):
        """Create NSI Première courses (4 grands thèmes)"""
        
        # 1. Programmation
        Course.objects.get_or_create(
            slug='nsi-programmation-premiere',
            defaults={
                'title': 'NSI - Programmation Python',
                'level': 'PREMIERE',
                'description': 'Bases de la programmation : variables, fonctions, tests, boucles',
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Programmation créé')
        
        # 2. Représentation des données
        Course.objects.get_or_create(
            slug='nsi-representation-donnees-premiere',
            defaults={
                'title': 'NSI - Représentation des Données',
                'level': 'PREMIERE',
                'description': 'Binaire, encodages, types de données, booléens',
                'order': 2,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Représentation créé')
        
        # 3. Traitement de données en tables
        Course.objects.get_or_create(
            slug='nsi-traitement-tables-premiere',
            defaults={
                'title': 'NSI - Traitement de Données',
                'level': 'PREMIERE',
                'description': 'Tables, CSV, recherche, tri, fusion de tables',
                'order': 3,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Traitement données créé')
        
        # 4. Algorithmique
        Course.objects.get_or_create(
            slug='nsi-algorithmique-premiere',
            defaults={
                'title': 'NSI - Algorithmique',
                'level': 'PREMIERE',
                'description': 'Algorithmes de parcours, recherche, tri, complexité',
                'order': 4,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Algorithmique créé')
        
        # 5. Architecture matérielle
        Course.objects.get_or_create(
            slug='nsi-architecture-premiere',
            defaults={
                'title': 'NSI - Architecture Matérielle',
                'level': 'PREMIERE',
                'description': 'Von Neumann, CPU, mémoire, systèmes d\'exploitation',
                'order': 5,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Architecture créé')
        
        # 6. Réseaux
        Course.objects.get_or_create(
            slug='nsi-reseaux-premiere',
            defaults={
                'title': 'NSI - Réseaux',
                'level': 'PREMIERE',
                'description': 'Protocoles, routage, TCP/IP, DNS, HTTP',
                'order': 6,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Réseaux créé')
        
        # 7. Web
        Course.objects.get_or_create(
            slug='nsi-web-premiere',
            defaults={
                'title': 'NSI - Web',
                'level': 'PREMIERE',
                'description': 'HTML, CSS, JavaScript, interactions client-serveur',
                'order': 7,
                'is_published': True,
            }
        )
        self.stdout.write('  ✓ Cours NSI Web créé')
