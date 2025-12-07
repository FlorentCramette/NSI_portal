from django.core.management.base import BaseCommand
from gamification.models import Badge, Achievement


class Command(BaseCommand):
    help = 'Initialize default badges and achievements'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating default badges...')
        
        badges_data = [
            {
                'code': 'BEGINNER',
                'name': 'Débutant',
                'description': 'Premiers pas dans l\'aventure',
                'icon': '🌱',
                'xp_requirement': 0,
                'order': 1
            },
            {
                'code': 'EXPLORER',
                'name': 'Explorateur',
                'description': 'Gagner 100 XP',
                'icon': '🧭',
                'xp_requirement': 100,
                'order': 2
            },
            {
                'code': 'SCHOLAR',
                'name': 'Érudit',
                'description': 'Gagner 500 XP',
                'icon': '📚',
                'xp_requirement': 500,
                'order': 3
            },
            {
                'code': 'EXPERT',
                'name': 'Expert',
                'description': 'Gagner 1000 XP',
                'icon': '🎓',
                'xp_requirement': 1000,
                'order': 4
            },
            {
                'code': 'MASTER',
                'name': 'Maître',
                'description': 'Gagner 2000 XP',
                'icon': '👑',
                'xp_requirement': 2000,
                'order': 5
            },
            {
                'code': 'LEGEND',
                'name': 'Légende',
                'description': 'Gagner 5000 XP',
                'icon': '⭐',
                'xp_requirement': 5000,
                'order': 6
            }
        ]
        
        badges_created = 0
        for badge_data in badges_data:
            badge, created = Badge.objects.get_or_create(
                code=badge_data['code'],
                defaults=badge_data
            )
            if created:
                badges_created += 1
                self.stdout.write(f"  ✓ Created badge: {badge.name}")
            else:
                self.stdout.write(f"  - Badge already exists: {badge.name}")
        
        self.stdout.write('Creating default achievements...')
        
        achievements_data = [
            {
                'code': 'FIRST_EXERCISE',
                'name': 'Premier pas',
                'description': 'Réussir votre premier exercice',
                'icon': '🎯',
                'xp_reward': 50
            },
            {
                'code': 'TEN_EXERCISES',
                'name': 'Persévérant',
                'description': 'Réussir 10 exercices différents',
                'icon': '🔟',
                'xp_reward': 100
            },
            {
                'code': 'PERFECT_SCORE',
                'name': 'Perfectionniste',
                'description': 'Obtenir un score parfait',
                'icon': '💯',
                'xp_reward': 75
            },
            {
                'code': 'WEEK_STREAK',
                'name': 'Régulier',
                'description': 'Connexion 7 jours d\'affilée',
                'icon': '🔥',
                'xp_reward': 150
            }
        ]
        
        achievements_created = 0
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                code=achievement_data['code'],
                defaults=achievement_data
            )
            if created:
                achievements_created += 1
                self.stdout.write(f"  ✓ Created achievement: {achievement.name}")
            else:
                self.stdout.write(f"  - Achievement already exists: {achievement.name}")
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nCreated {badges_created} badges and {achievements_created} achievements'
            )
        )
