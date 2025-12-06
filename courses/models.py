from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    """A course (SNT for Seconde, NSI for Première/Terminale)"""

    class Level(models.TextChoices):
        SNT = 'SNT', 'SNT (Seconde)'
        PREMIERE = 'PREMIERE', 'NSI Première'
        TERMINALE = 'TERMINALE', 'NSI Terminale'

    title = models.CharField(max_length=200, verbose_name='Titre')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Slug')
    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        verbose_name='Niveau'
    )
    description = models.TextField(verbose_name='Description')
    icon = models.CharField(max_length=10, default='📚', verbose_name='Icône')
    image_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="URL de l'image")
    order = models.IntegerField(default=0, verbose_name='Ordre')
    is_published = models.BooleanField(default=False, verbose_name='Publié')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
        ordering = ['level', 'order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_level_display()} - {self.title}"
class Chapter(models.Model):
    """A chapter within a course"""
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='chapters'
    )
    title = models.CharField(max_length=200, verbose_name='Titre')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, verbose_name='Description')
    order = models.IntegerField(default=0, verbose_name='Ordre')
    is_published = models.BooleanField(default=False, verbose_name='Publié')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'
        ordering = ['course', 'order']
        unique_together = ['course', 'slug']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_completion_for_user(self, user):
        """Calculate completion percentage for a specific user"""
        from exercises.models import Exercise, Attempt
        
        exercises = Exercise.objects.filter(chapter=self)
        if not exercises.exists():
            return 100
        
        completed = Attempt.objects.filter(
            user=user,
            exercise__chapter=self,
            passed=True
        ).values('exercise').distinct().count()
        
        return int((completed / exercises.count()) * 100)


class ContentBlock(models.Model):
    """A block of content within a chapter"""
    
    class BlockType(models.TextChoices):
        TEXT = 'TEXT', 'Texte'
        CODE_SAMPLE = 'CODE_SAMPLE', 'Exemple de code'
        EXERCISE = 'EXERCISE', 'Exercice'
        QUIZ = 'QUIZ', 'Quiz'
        VIDEO = 'VIDEO', 'Vidéo'
    
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name='content_blocks'
    )
    type = models.CharField(
        max_length=20,
        choices=BlockType.choices,
        verbose_name='Type'
    )
    title = models.CharField(max_length=200, blank=True, verbose_name='Titre')
    content_markdown = models.TextField(verbose_name='Contenu (Markdown)')
    order = models.IntegerField(default=0, verbose_name='Ordre')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Bloc de contenu'
        verbose_name_plural = 'Blocs de contenu'
        ordering = ['chapter', 'order']
    
    def __str__(self):
        return f"{self.chapter.title} - {self.get_type_display()} #{self.order}"


class ChapterAssignment(models.Model):
    """Assigns a chapter to a classroom"""
    
    classroom = models.ForeignKey(
        'accounts.Classroom',
        on_delete=models.CASCADE,
        related_name='chapter_assignments'
    )
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True, verbose_name='Date limite')
    
    class Meta:
        verbose_name = 'Attribution de chapitre'
        verbose_name_plural = 'Attributions de chapitres'
        unique_together = ['classroom', 'chapter']
        ordering = ['-assigned_at']
    
    def __str__(self):
        return f"{self.chapter} → {self.classroom.name}"

