from django.db import models


class Exercise(models.Model):
    """An exercise (Python, SQL, MCQ, or Parsons)"""
    
    class ExerciseType(models.TextChoices):
        PYTHON = 'PYTHON', 'Python'
        SQL = 'SQL', 'SQL'
        MCQ = 'MCQ', 'QCM'
        PARSONS = 'PARSONS', 'Parsons (réorganisation)'
    
    chapter = models.ForeignKey(
        'courses.Chapter',
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    title = models.CharField(max_length=200, verbose_name='Titre')
    type = models.CharField(
        max_length=10,
        choices=ExerciseType.choices,
        verbose_name='Type'
    )
    statement_markdown = models.TextField(verbose_name='Énoncé (Markdown)')
    starter_code = models.TextField(blank=True, verbose_name='Code de départ')
    tests_definition = models.JSONField(
        default=dict,
        verbose_name='Définition des tests (JSON)',
        help_text='Pour Python: liste de tests. Pour SQL: schéma et requêtes. Pour MCQ: questions et réponses.'
    )
    xp_reward = models.IntegerField(default=10, verbose_name='XP récompensé')
    order = models.IntegerField(default=0, verbose_name='Ordre')
    is_published = models.BooleanField(default=False, verbose_name='Publié')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'
        ordering = ['chapter', 'order']
    
    def __str__(self):
        return f"{self.chapter.title} - {self.title}"
    
    def get_success_rate(self):
        """Calculate success rate for this exercise"""
        attempts = self.attempts.count()
        if attempts == 0:
            return 0
        passed = self.attempts.filter(passed=True).count()
        return int((passed / attempts) * 100)
    
    def has_user_passed(self, user):
        """Check if user has successfully completed this exercise"""
        return self.attempts.filter(user=user, passed=True).exists()


class Attempt(models.Model):
    """A student's attempt at an exercise"""
    
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='attempts'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='attempts'
    )
    passed = models.BooleanField(default=False, verbose_name='Réussi')
    score = models.IntegerField(default=0, verbose_name='Score')
    attempt_data = models.JSONField(
        default=dict,
        verbose_name='Données de la tentative',
        help_text='Code soumis, réponses, temps passé, etc.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tentative'
        verbose_name_plural = 'Tentatives'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'exercise', 'passed']),
        ]
    
    def __str__(self):
        status = "✓" if self.passed else "✗"
        return f"{status} {self.user} - {self.exercise.title} ({self.score}%)"


class Hint(models.Model):
    """A hint for an exercise"""
    
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='hints'
    )
    content = models.TextField(verbose_name='Contenu de l\'indice')
    order = models.IntegerField(default=0, verbose_name='Ordre')
    xp_cost = models.IntegerField(
        default=0,
        verbose_name='Coût en XP',
        help_text='XP déduits si l\'élève utilise cet indice'
    )
    
    class Meta:
        verbose_name = 'Indice'
        verbose_name_plural = 'Indices'
        ordering = ['exercise', 'order']
    
    def __str__(self):
        return f"Indice #{self.order} - {self.exercise.title}"


class HintUsage(models.Model):
    """Track when a user uses a hint"""
    
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='hint_usages'
    )
    hint = models.ForeignKey(
        Hint,
        on_delete=models.CASCADE,
        related_name='usages'
    )
    used_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Utilisation d\'indice'
        verbose_name_plural = 'Utilisations d\'indices'
        unique_together = ['user', 'hint']
        ordering = ['-used_at']
    
    def __str__(self):
        return f"{self.user} - {self.hint}"
