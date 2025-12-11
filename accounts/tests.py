"""
Tests for accounts models
"""
from typing import TYPE_CHECKING
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Classroom, Enrollment

if TYPE_CHECKING:
    from accounts.models import User
    UserType = User
else:
    User = get_user_model()
    UserType = User


class UserModelTest(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(
            username='test_student',
            password='test123',
            role=User.Role.STUDENT,
            pseudo='TestStudent'
        )
        
        self.teacher = User.objects.create_user(
            username='test_teacher',
            password='test123',
            role=User.Role.TEACHER
        )
    
    def test_user_creation(self):
        """Test that users are created correctly"""
        self.assertEqual(self.student.username, 'test_student')
        self.assertEqual(self.student.role, User.Role.STUDENT)
        self.assertEqual(self.student.pseudo, 'TestStudent')
        self.assertEqual(self.student.xp, 0)
        self.assertEqual(self.student.level, 1)
    
    def test_add_xp(self):
        """Test XP addition and level up"""
        self.student.add_xp(50)
        self.assertEqual(self.student.xp, 50)
        self.assertEqual(self.student.level, 1)
        
        # Add enough XP to level up (100 XP for level 2)
        self.student.add_xp(60)
        self.assertEqual(self.student.xp, 110)
        self.assertEqual(self.student.level, 2)
        
        # Add enough for level 3 (200 XP total needed)
        self.student.add_xp(100)
        self.assertEqual(self.student.xp, 210)
        self.assertEqual(self.student.level, 3)
    
    def test_role_choices(self):
        """Test role field choices"""
        self.assertEqual(self.student.role, 'STUDENT')
        self.assertEqual(self.teacher.role, 'TEACHER')


class ClassroomModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='test_teacher',
            password='test123',
            role=User.Role.TEACHER
        )
        
        self.classroom = Classroom.objects.create(
            name='Test Class',
            school_name='Test School',
            teacher=self.teacher
        )
    
    def test_classroom_creation(self):
        """Test classroom is created with join code"""
        self.assertEqual(self.classroom.name, 'Test Class')
        self.assertEqual(self.classroom.school_name, 'Test School')
        self.assertIsNotNone(self.classroom.join_code)
        self.assertEqual(len(self.classroom.join_code), 6)
    
    def test_join_code_unique(self):
        """Test that join codes are unique"""
        classroom2 = Classroom.objects.create(
            name='Test Class 2',
            school_name='Test School',
            teacher=self.teacher
        )
        self.assertNotEqual(self.classroom.join_code, classroom2.join_code)
    
    def test_student_enrollment(self):
        """Test enrolling students in classroom"""
        student = User.objects.create_user(
            username='test_student',
            password='test123',
            role=User.Role.STUDENT
        )
        
        Enrollment.objects.create(
            user=student,
            classroom=self.classroom
        )
        
        # Test using the get_students() method
        students = self.classroom.get_students()
        self.assertEqual(students.count(), 1)
        self.assertEqual(students.first(), student)
        
        # Test reverse relation through enrollment
        self.assertEqual(student.enrollments.count(), 1)
        self.assertEqual(student.enrollments.first().classroom, self.classroom)
