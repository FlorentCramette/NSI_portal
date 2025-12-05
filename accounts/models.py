from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
import string


class User(AbstractUser):
    """Custom User model with role-based access"""
    
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Élève'
        TEACHER = 'TEACHER', 'Professeur'
        ADMIN = 'ADMIN', 'Administrateur'
    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )
    pseudo = models.CharField(max_length=50, blank=True, null=True)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
    
    def __str__(self):
        if self.role == self.Role.STUDENT and self.pseudo:
            return self.pseudo
        return self.username
    
    def add_xp(self, points):
        """Add XP and check for level up"""
        self.xp += points
        new_level = (self.xp // 100) + 1
        if new_level > self.level:
            self.level = new_level
        self.save()
    
    @property
    def is_student(self):
        return self.role == self.Role.STUDENT
    
    @property
    def is_teacher(self):
        return self.role == self.Role.TEACHER
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN


def generate_join_code():
    """Generate a unique 6-character classroom join code"""
    return get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)


class Classroom(models.Model):
    """A classroom managed by a teacher"""
    
    name = models.CharField(max_length=100, verbose_name='Nom de la classe')
    school_name = models.CharField(max_length=200, verbose_name='Établissement')
    join_code = models.CharField(
        max_length=6,
        unique=True,
        default=generate_join_code,
        verbose_name='Code de classe'
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='classrooms_taught',
        limit_choices_to={'role': User.Role.TEACHER}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.school_name}"
    
    def get_students(self):
        """Get all students enrolled in this classroom"""
        return User.objects.filter(enrollments__classroom=self)


class Enrollment(models.Model):
    """Links students to classrooms"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments',
        limit_choices_to={'role': User.Role.STUDENT}
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Inscription'
        verbose_name_plural = 'Inscriptions'
        unique_together = ['user', 'classroom']
        ordering = ['-enrolled_at']
    
    def __str__(self):
        return f"{self.user} → {self.classroom.name}"
