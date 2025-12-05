from django.db import models


class Badge(models.Model):
    """A badge that can be earned"""
    
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Code',
        help_text='Identifiant unique du badge'
    )
    name = models.CharField(max_length=100, verbose_name='Nom')
    description = models.TextField(verbose_name='Description')
    icon = models.CharField(
        max_length=50,
        default='🏆',
        verbose_name='Icône',
        help_text='Emoji ou classe CSS pour l\'icône'
    )
    xp_requirement = models.IntegerField(
        default=0,
        verbose_name='XP requis',
        help_text='XP nécessaire pour débloquer ce badge'
    )
    order = models.IntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.icon} {self.name}"
    
    def check_and_award(self, user):
        """Check if user qualifies for this badge and award it"""
        if self.xp_requirement > 0 and user.xp < self.xp_requirement:
            return False
        
        # Check if user already has this badge
        if UserBadge.objects.filter(user=user, badge=self).exists():
            return False
        
        # Award the badge
        UserBadge.objects.create(user=user, badge=self)
        return True


class UserBadge(models.Model):
    """Links users to earned badges"""
    
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='earned_badges'
    )
    badge = models.ForeignKey(
        Badge,
        on_delete=models.CASCADE,
        related_name='user_badges'
    )
    earned_at = models.DateTimeField(auto_now_add=True, verbose_name='Obtenu le')
    
    class Meta:
        verbose_name = 'Badge utilisateur'
        verbose_name_plural = 'Badges utilisateurs'
        unique_together = ['user', 'badge']
        ordering = ['-earned_at']
    
    def __str__(self):
        return f"{self.user} - {self.badge.name}"


class Streak(models.Model):
    """Track daily login streaks for users"""
    
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='streak'
    )
    current_streak = models.IntegerField(default=0, verbose_name='Série actuelle')
    longest_streak = models.IntegerField(default=0, verbose_name='Meilleure série')
    last_activity_date = models.DateField(null=True, blank=True, verbose_name='Dernière activité')
    
    class Meta:
        verbose_name = 'Série de connexions'
        verbose_name_plural = 'Séries de connexions'
    
    def __str__(self):
        return f"{self.user} - {self.current_streak} jours"
    
    def update_streak(self, activity_date=None):
        """Update streak based on activity date"""
        from datetime import date, timedelta
        
        if activity_date is None:
            activity_date = date.today()
        
        if self.last_activity_date is None:
            # First activity
            self.current_streak = 1
            self.longest_streak = 1
        elif activity_date == self.last_activity_date:
            # Same day, no change
            return
        elif activity_date == self.last_activity_date + timedelta(days=1):
            # Consecutive day
            self.current_streak += 1
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
        else:
            # Streak broken
            self.current_streak = 1
        
        self.last_activity_date = activity_date
        self.save()


class Achievement(models.Model):
    """Track specific achievements (first exercise, 10 exercises, etc.)"""
    
    code = models.CharField(max_length=50, unique=True, verbose_name='Code')
    name = models.CharField(max_length=100, verbose_name='Nom')
    description = models.TextField(verbose_name='Description')
    icon = models.CharField(max_length=50, default='⭐', verbose_name='Icône')
    xp_reward = models.IntegerField(default=50, verbose_name='XP récompensé')
    
    class Meta:
        verbose_name = 'Accomplissement'
        verbose_name_plural = 'Accomplissements'
    
    def __str__(self):
        return f"{self.icon} {self.name}"


class UserAchievement(models.Model):
    """Track which achievements users have earned"""
    
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='achievements'
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name='user_achievements'
    )
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Accomplissement utilisateur'
        verbose_name_plural = 'Accomplissements utilisateurs'
        unique_together = ['user', 'achievement']
        ordering = ['-earned_at']
    
    def __str__(self):
        return f"{self.user} - {self.achievement.name}"
