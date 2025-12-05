from django.contrib import admin
from .models import Exercise, Attempt, Hint, HintUsage


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'chapter', 'xp_reward', 'order', 'is_published']
    list_filter = ['type', 'is_published', 'chapter__course']
    search_fields = ['title', 'statement_markdown']


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise', 'passed', 'score', 'created_at']
    list_filter = ['passed', 'exercise__type', 'created_at']
    search_fields = ['user__username', 'user__pseudo', 'exercise__title']
    readonly_fields = ['created_at']


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'order', 'xp_cost']
    list_filter = ['exercise__chapter']
    search_fields = ['exercise__title', 'content']


@admin.register(HintUsage)
class HintUsageAdmin(admin.ModelAdmin):
    list_display = ['user', 'hint', 'used_at']
    list_filter = ['used_at']
    search_fields = ['user__username', 'hint__exercise__title']
    readonly_fields = ['used_at']
