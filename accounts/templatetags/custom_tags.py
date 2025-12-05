"""
Custom template tags for NSI Portal
"""
from django import template
from django.db.models import Count, Avg
from exercises.models import Attempt

register = template.Library()


@register.filter
def total_students(classrooms):
    """Get total number of students across classrooms"""
    total = 0
    for classroom in classrooms:
        total += classroom.students.count()
    return total


@register.filter
def total_attempts(classrooms):
    """Get total number of attempts by students in classrooms"""
    student_ids = []
    for classroom in classrooms:
        student_ids.extend(classroom.students.values_list('id', flat=True))
    return Attempt.objects.filter(user_id__in=student_ids).count()


@register.filter
def success_rate(classrooms):
    """Calculate average success rate across classrooms"""
    student_ids = []
    for classroom in classrooms:
        student_ids.extend(classroom.students.values_list('id', flat=True))
    
    attempts = Attempt.objects.filter(user_id__in=student_ids)
    total = attempts.count()
    if total == 0:
        return 0
    passed = attempts.filter(passed=True).count()
    return round((passed / total) * 100, 1)


@register.filter
def total_exercises_solved(user):
    """Get number of unique exercises solved by user"""
    return user.attempts.filter(passed=True).values('exercise').distinct().count()


@register.filter
def total_attempts_count(user):
    """Get total number of attempts by user"""
    return user.attempts.count()


@register.filter
def user_success_rate(user):
    """Calculate user's success rate"""
    total = user.attempts.count()
    if total == 0:
        return 0
    passed = user.attempts.filter(passed=True).count()
    return round((passed / total) * 100, 1)


@register.filter
def xp_to_next_level(user):
    """Calculate XP needed for next level"""
    next_level = user.level + 1
    required_xp = next_level * 100
    return required_xp - user.xp


@register.filter
def level_progress_percentage(user):
    """Calculate progress percentage to next level"""
    current_level_xp = user.level * 100
    next_level_xp = (user.level + 1) * 100
    level_range = next_level_xp - current_level_xp
    progress = user.xp - current_level_xp
    if level_range == 0:
        return 0
    return round((progress / level_range) * 100, 1)
