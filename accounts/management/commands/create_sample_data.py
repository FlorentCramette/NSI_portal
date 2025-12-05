"""
Management command to create sample data for testing
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Classroom, Enrollment
from courses.models import Course, Chapter, ContentBlock
from exercises.models import Exercise
from gamification.models import Badge, Achievement

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create users
        admin, _ = User.objects.get_or_create(
            username='admin',
            defaults={
                'role': User.Role.ADMIN,
                'is_staff': True,
                'is_superuser': True,
            }
        )
        admin.set_password('admin123')
        admin.save()
        self.stdout.write(self.style.SUCCESS('✓ Admin user created'))

        teacher, _ = User.objects.get_or_create(
            username='prof_martin',
            defaults={
                'role': User.Role.TEACHER,
                'email': 'martin@lycee.fr',
                'first_name': 'Jean',
                'last_name': 'Martin',
            }
        )
        teacher.set_password('prof123')
        teacher.save()
        self.stdout.write(self.style.SUCCESS('✓ Teacher created'))

        student, _ = User.objects.get_or_create(
            username='eleve_alice',
            defaults={
                'role': User.Role.STUDENT,
                'pseudo': 'Alice',
            }
        )
        student.set_password('eleve123')
        student.save()
        self.stdout.write(self.style.SUCCESS('✓ Student created'))

        # Create classroom
        classroom, _ = Classroom.objects.get_or_create(
            name='NSI Terminale 1',
            school_name='Lycée Victor Hugo',
            teacher=teacher
        )
        Enrollment.objects.get_or_create(user=student, classroom=classroom)
        self.stdout.write(self.style.SUCCESS(f'✓ Classroom created with code: {classroom.join_code}'))

        # Create course
        course, _ = Course.objects.get_or_create(
            title='Python et Algorithmique',
            level=Course.Level.PREMIERE,
            defaults={
                'description': 'Introduction à Python et aux algorithmes de base',
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Course created'))

        # Create chapter
        chapter, _ = Chapter.objects.get_or_create(
            course=course,
            slug='introduction-python',
            defaults={
                'title': 'Introduction à Python',
                'description': 'Les bases du langage Python',
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Chapter created'))

        # Create content blocks
        ContentBlock.objects.get_or_create(
            chapter=chapter,
            order=1,
            defaults={
                'type': ContentBlock.BlockType.TEXT,
                'title': 'Variables et types',
                'content_markdown': '''# Variables en Python

En Python, on peut créer des variables sans déclarer leur type :

```python
nombre = 42
texte = "Bonjour"
decimal = 3.14
```
''',
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Content block created'))

        # Create Python exercise
        Exercise.objects.get_or_create(
            chapter=chapter,
            title='Calculer une somme',
            defaults={
                'type': Exercise.ExerciseType.PYTHON,
                'statement_markdown': '''Écrivez une fonction `calculer_somme(a, b)` qui retourne la somme de deux nombres.

**Exemple:**
```python
calculer_somme(5, 3)  # Doit retourner 8
```
''',
                'starter_code': '''def calculer_somme(a, b):
    # À compléter
    pass
''',
                'tests_definition': {
                    'tests': [
                        {
                            'name': 'Test 1 : Nombres positifs',
                            'code': 'calculer_somme(5, 3)',
                            'expected': 8
                        },
                        {
                            'name': 'Test 2 : Nombres négatifs',
                            'code': 'calculer_somme(-2, -3)',
                            'expected': -5
                        },
                        {
                            'name': 'Test 3 : Zéro',
                            'code': 'calculer_somme(0, 10)',
                            'expected': 10
                        }
                    ]
                },
                'xp_reward': 10,
                'order': 1,
                'is_published': True,
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Exercise created'))

        # Create badges
        Badge.objects.get_or_create(
            code='BEGINNER',
            defaults={
                'name': 'Débutant',
                'description': 'Commencer votre aventure NSI',
                'icon': '🌱',
                'xp_requirement': 0,
                'order': 1,
                'is_active': True,
            }
        )
        Badge.objects.get_or_create(
            code='BRONZE',
            defaults={
                'name': 'Badge Bronze',
                'description': 'Atteindre 100 XP',
                'icon': '🥉',
                'xp_requirement': 100,
                'order': 2,
                'is_active': True,
            }
        )
        Badge.objects.get_or_create(
            code='SILVER',
            defaults={
                'name': 'Badge Argent',
                'description': 'Atteindre 500 XP',
                'icon': '🥈',
                'xp_requirement': 500,
                'order': 3,
                'is_active': True,
            }
        )
        Badge.objects.get_or_create(
            code='GOLD',
            defaults={
                'name': 'Badge Or',
                'description': 'Atteindre 1000 XP',
                'icon': '🥇',
                'xp_requirement': 1000,
                'order': 4,
                'is_active': True,
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Badges created'))

        # Create achievements
        Achievement.objects.get_or_create(
            code='FIRST_EXERCISE',
            defaults={
                'name': 'Premier pas',
                'description': 'Réussir votre premier exercice',
                'icon': '🎯',
                'xp_reward': 50,
            }
        )
        Achievement.objects.get_or_create(
            code='TEN_EXERCISES',
            defaults={
                'name': 'Persévérant',
                'description': 'Réussir 10 exercices différents',
                'icon': '🔟',
                'xp_reward': 100,
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Achievements created'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample data created successfully!'))
        self.stdout.write('\nLogin credentials:')
        self.stdout.write('  Admin: admin / admin123')
        self.stdout.write('  Teacher: prof_martin / prof123')
        self.stdout.write(f'  Student: eleve_alice / eleve123 (Classroom code: {classroom.join_code})')
