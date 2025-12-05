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
    
    # First exercise completed
    if user.attempts.filter(passed=True).count() == 1:
        achievement, created = Achievement.objects.get_or_create(
            code='FIRST_EXERCISE',
            defaults={
                'name': 'Premier pas',
                'description': 'Réussir votre premier exercice',
                'icon': '🎯',
                'xp_reward': 50
            }
        )
        if created or not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.get_or_create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    # 10 exercises completed
    if user.attempts.filter(passed=True).values('exercise').distinct().count() == 10:
        achievement, created = Achievement.objects.get_or_create(
            code='TEN_EXERCISES',
            defaults={
                'name': 'Persévérant',
                'description': 'Réussir 10 exercices différents',
                'icon': '🔟',
                'xp_reward': 100
            }
        )
        if created or not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            UserAchievement.objects.get_or_create(user=user, achievement=achievement)
            user.add_xp(achievement.xp_reward)
            achievements_awarded.append(achievement)
    
    return achievements_awarded


def update_user_streak(user):
    """Update user's daily login streak"""
    streak, created = Streak.objects.get_or_create(user=user)
    streak.update_streak(date.today())
    return streak
