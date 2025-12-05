from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Classroom, Enrollment


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'pseudo', 'email', 'role', 'xp', 'level', 'is_active']
    list_filter = ['role', 'is_active', 'is_staff']
    search_fields = ['username', 'pseudo', 'email', 'first_name', 'last_name']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informations NSI', {
            'fields': ('role', 'pseudo', 'xp', 'level')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informations NSI', {
            'fields': ('role', 'pseudo')
        }),
    )


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'school_name', 'teacher', 'join_code', 'created_at']
    list_filter = ['school_name', 'created_at']
    search_fields = ['name', 'school_name', 'join_code', 'teacher__username']
    readonly_fields = ['join_code', 'created_at', 'updated_at']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'classroom', 'enrolled_at']
    list_filter = ['classroom', 'enrolled_at']
    search_fields = ['user__username', 'user__pseudo', 'classroom__name']
    readonly_fields = ['enrolled_at']
