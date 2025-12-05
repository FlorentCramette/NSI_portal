from django.contrib import admin
from .models import Badge, UserBadge, Streak, Achievement, UserAchievement


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'xp_requirement', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'code', 'description']


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge', 'earned_at']
    list_filter = ['badge', 'earned_at']
    search_fields = ['user__username', 'user__pseudo', 'badge__name']
    readonly_fields = ['earned_at']


@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_streak', 'longest_streak', 'last_activity_date']
    search_fields = ['user__username', 'user__pseudo']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'xp_reward']
    search_fields = ['name', 'code', 'description']


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'earned_at']
    list_filter = ['achievement', 'earned_at']
    search_fields = ['user__username', 'user__pseudo', 'achievement__name']
    readonly_fields = ['earned_at']
