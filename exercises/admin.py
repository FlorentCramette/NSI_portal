from django.contrib import admin
from .models import (
    Exercise, Attempt, Hint, HintUsage,
    Assessment, AssessmentQuestion, AssessmentResult, ClassroomAssessmentStats
)


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


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'course', 'duration_minutes', 'passing_score', 'is_published']
    list_filter = ['type', 'is_published', 'course__level']
    search_fields = ['title', 'description']


@admin.register(AssessmentQuestion)
class AssessmentQuestionAdmin(admin.ModelAdmin):
    list_display = ['assessment', 'exercise', 'points', 'order']
    list_filter = ['assessment__type', 'assessment__course']
    search_fields = ['assessment__title', 'exercise__title']


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'assessment', 'score', 'points_earned', 'points_total', 'completed_at']
    list_filter = ['assessment__type', 'assessment__course', 'completed_at']
    search_fields = ['user__username', 'user__pseudo', 'assessment__title']
    readonly_fields = ['started_at', 'completed_at']


@admin.register(ClassroomAssessmentStats)
class ClassroomAssessmentStatsAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'assessment', 'average_score', 'students_passed', 'students_total', 'completion_rate']
    list_filter = ['assessment__type', 'assessment__course']
    search_fields = ['classroom__name', 'assessment__title']
    readonly_fields = ['last_updated']
