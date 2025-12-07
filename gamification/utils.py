"""
Utility functions for gamification features
"""
from gamification.models import Badge, Achievement, UserAchievement, Streak
from datetime import date


def check_and_award_badges(user):
    """Check all active badges and award if user qualifies"""
    badges_awarded = []
    
    for badge in Badge.objects.filter(is_active=True):
        if badge.check_and_award(user):
            badges_awarded.append(badge)
    
    return badges_awarded


def check_achievements(user):
    """Check and award achievements based on user activity"""
    achievements_awarded = []
    
    # Count distinct exercises passed
    exercises_passed = user.attempts.filter(passed=True).values('exercise').distinct().count()
    
    # First exercise completed
    if exercises_passed == 1:
        achievement, created = Achievement.objects.get_or_create(
            code='FIRST_EXERCISE',
            defaults={
                'name': 'Premier pas',
                'description': 'Réussir votre premier exercice',
                'icon': '🎯',
                'xp_reward': 50
            }
        )
        if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    # 10 exercises completed
    if exercises_passed >= 10:
        achievement, created = Achievement.objects.get_or_create(
            code='TEN_EXERCISES',
            defaults={
                'name': 'Persévérant',
                'description': 'Réussir 10 exercices différents',
                'icon': '🔟',
                'xp_reward': 100
            }
        )
        if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    # Perfect score achievement
    latest_attempt = user.attempts.filter(passed=True).order_by('-created_at').first()
    if latest_attempt and latest_attempt.score == 100:
        achievement, created = Achievement.objects.get_or_create(
            code='PERFECT_SCORE',
            defaults={
                'name': 'Perfectionniste',
                'description': 'Obtenir un score parfait',
                'icon': '💯',
                'xp_reward': 75
            }
        )
        if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    # Week streak achievement
    if hasattr(user, 'streak') and user.streak.current_streak >= 7:
        achievement, created = Achievement.objects.get_or_create(
            code='WEEK_STREAK',
            defaults={
                'name': 'Régulier',
                'description': 'Connexion 7 jours d\'affilée',
                'icon': '🔥',
                'xp_reward': 150
            }
        )
        if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    return achievements_awarded


def update_user_streak(user):
    """Update user's daily login streak"""
    streak, created = Streak.objects.get_or_create(user=user)
    streak.update_streak(date.today())
    return streak
