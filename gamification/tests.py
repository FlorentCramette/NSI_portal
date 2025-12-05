"""
Tests for gamification models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from gamification.models import Badge, UserBadge, Achievement, UserAchievement

User = get_user_model()


class BadgeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_student',
            password='test123',
            role=User.Role.STUDENT
        )
        
        self.badge_bronze = Badge.objects.create(
            name='Bronze',
            code='BRONZE',
            description='Reach 100 XP',
            icon='🥉',
            xp_requirement=100,
            is_active=True
        )
        
        self.badge_silver = Badge.objects.create(
            name='Silver',
            code='SILVER',
            description='Reach 500 XP',
            icon='🥈',
            xp_requirement=500,
            is_active=True
        )
    
    def test_badge_creation(self):
        """Test badge is created correctly"""
        self.assertEqual(self.badge_bronze.name, 'Bronze')
        self.assertEqual(self.badge_bronze.xp_requirement, 100)
        self.assertTrue(self.badge_bronze.is_active)
    
    def test_badge_not_awarded_insufficient_xp(self):
        """Test badge is not awarded without enough XP"""
        self.user.xp = 50
        self.user.save()
        
        awarded = self.badge_bronze.check_and_award(self.user)
        self.assertFalse(awarded)
        self.assertEqual(self.user.earned_badges.count(), 0)
    
    def test_badge_awarded_sufficient_xp(self):
        """Test badge is awarded with enough XP"""
        self.user.xp = 150
        self.user.save()
        
        awarded = self.badge_bronze.check_and_award(self.user)
        self.assertTrue(awarded)
        self.assertEqual(self.user.earned_badges.count(), 1)
    
    def test_badge_not_awarded_twice(self):
        """Test badge is not awarded twice"""
        self.user.xp = 150
        self.user.save()
        
        # Award first time
        self.badge_bronze.check_and_award(self.user)
        
        # Try to award again
        awarded = self.badge_bronze.check_and_award(self.user)
        self.assertFalse(awarded)
        self.assertEqual(self.user.earned_badges.count(), 1)


class AchievementModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_student',
            password='test123',
            role=User.Role.STUDENT
        )
        
        self.achievement = Achievement.objects.create(
            name='First Exercise',
            code='FIRST_EXERCISE',
            description='Complete your first exercise',
            icon='🎯',
            xp_reward=50
        )
    
    def test_achievement_creation(self):
        """Test achievement is created correctly"""
        self.assertEqual(self.achievement.name, 'First Exercise')
        self.assertEqual(self.achievement.xp_reward, 50)
    
    def test_user_achievement(self):
        """Test awarding achievement to user"""
        UserAchievement.objects.create(
            user=self.user,
            achievement=self.achievement
        )
        
        self.assertEqual(self.user.achievements.count(), 1)
        self.assertEqual(
            self.user.achievements.first().achievement.code,
            'FIRST_EXERCISE'
        )
