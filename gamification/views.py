from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Count, Q
from .models import Badge, UserBadge
from accounts.models import User


class BadgeListView(LoginRequiredMixin, ListView):
    """List all badges"""
    model = Badge
    template_name = 'gamification/badge_list.html'
    context_object_name = 'badges'
    
    def get_queryset(self):
        return Badge.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Get user's earned badges
        earned_badge_ids = UserBadge.objects.filter(user=user).values_list('badge_id', flat=True)
        context['earned_badge_ids'] = list(earned_badge_ids)
        
        return context


class LeaderboardView(LoginRequiredMixin, ListView):
    """Display leaderboard of top users"""
    model = User
    template_name = 'gamification/leaderboard.html'
    context_object_name = 'users'
    paginate_by = 50
    
    def get_queryset(self):
        return User.objects.filter(
            role=User.Role.STUDENT,
            is_active=True
        ).annotate(
            badges_count=Count('earned_badges')
        ).order_by('-xp', '-level')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add user's rank
        user = self.request.user
        if user.is_student:
            users_above = User.objects.filter(
                role=User.Role.STUDENT,
                is_active=True,
                xp__gt=user.xp
            ).count()
            context['user_rank'] = users_above + 1
        
        return context
