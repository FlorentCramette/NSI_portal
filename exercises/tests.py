"""
Tests for exercise models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from courses.models import Course, Chapter
from exercises.models import Exercise, Attempt, Hint, HintUsage

User = get_user_model()


class ExerciseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_student',
            password='test123',
            role=User.Role.STUDENT
        )
        
        self.course = Course.objects.create(
            title='Test Course',
            level=Course.Level.PREMIERE,
            is_published=True
        )
        
        self.chapter = Chapter.objects.create(
            course=self.course,
            title='Test Chapter',
            slug='test-chapter',
            is_published=True
        )
        
        self.exercise = Exercise.objects.create(
            chapter=self.chapter,
            title='Test Exercise',
            type=Exercise.ExerciseType.PYTHON,
            statement_markdown='Test statement',
            starter_code='def test():\n    pass',
            tests_definition={'tests': []},
            xp_reward=10,
            is_published=True
        )
    
    def test_exercise_creation(self):
        """Test exercise is created correctly"""
        self.assertEqual(self.exercise.title, 'Test Exercise')
        self.assertEqual(self.exercise.type, 'PYTHON')
        self.assertEqual(self.exercise.xp_reward, 10)
        self.assertTrue(self.exercise.is_published)
    
    def test_attempt_creation(self):
        """Test attempt is created and scored"""
        attempt = Attempt.objects.create(
            exercise=self.exercise,
            user=self.user,
            submitted_code='def test():\n    return 42',
            score=100,
            passed=True,
            xp_earned=10
        )
        
        self.assertEqual(attempt.score, 100)
        self.assertTrue(attempt.passed)
        self.assertEqual(attempt.xp_earned, 10)
        self.assertEqual(self.user.attempts.count(), 1)
    
    def test_attempt_failed(self):
        """Test failed attempt"""
        attempt = Attempt.objects.create(
            exercise=self.exercise,
            user=self.user,
            submitted_code='def test():\n    return None',
            score=0,
            passed=False,
            xp_earned=0
        )
        
        self.assertFalse(attempt.passed)
        self.assertEqual(attempt.xp_earned, 0)
    
    def test_hint_usage(self):
        """Test hint usage tracking"""
        hint = Hint.objects.create(
            exercise=self.exercise,
            content='This is a hint',
            xp_cost=2,
            order=1
        )
        
        usage = HintUsage.objects.create(
            user=self.user,
            hint=hint
        )
        
        self.assertEqual(self.user.hints_used.count(), 1)
        self.assertEqual(usage.hint.content, 'This is a hint')
