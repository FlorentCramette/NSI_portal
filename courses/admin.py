from django.contrib import admin
from .models import Course, Chapter, ContentBlock, ChapterAssignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'order', 'is_published', 'created_at']
    list_filter = ['level', 'is_published']
    search_fields = ['title', 'description']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'is_published', 'created_at']
    list_filter = ['course', 'is_published']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'type', 'title', 'order']
    list_filter = ['type', 'chapter__course']
    search_fields = ['title', 'content_markdown']


@admin.register(ChapterAssignment)
class ChapterAssignmentAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'classroom', 'assigned_at', 'due_date']
    list_filter = ['classroom', 'assigned_at']
    search_fields = ['chapter__title', 'classroom__name']
