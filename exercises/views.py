from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView, ListView, View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Exercise, Attempt, Hint, HintUsage


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    """View an exercise and its details"""
    model = Exercise
    template_name = 'exercises/exercise_detail.html'
    context_object_name = 'exercise'
    
    def get_queryset(self):
        return Exercise.objects.filter(is_published=True).select_related('chapter__course')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = self.object
        user = self.request.user
        
        # Get user's previous attempts
        context['attempts'] = exercise.attempts.filter(user=user).order_by('-created_at')[:5]
        context['has_passed'] = exercise.has_user_passed(user)
        context['success_rate'] = exercise.get_success_rate()
        
        # Get hints
        context['hints'] = exercise.hints.all()
        context['used_hints'] = HintUsage.objects.filter(user=user, hint__exercise=exercise).values_list('hint_id', flat=True)
        
        return context


@method_decorator(csrf_exempt, name='dispatch')
class SubmitAttemptView(LoginRequiredMixin, View):
    """Submit an exercise attempt (AJAX endpoint)"""
    
    def post(self, request, pk):
        try:
            data = json.loads(request.body)
            exercise = get_object_or_404(Exercise, pk=pk)
            user = request.user
            
            passed = data.get('passed', False)
            score = data.get('score', 0)
            attempt_data = data.get('attempt_data', {})
            
            # Create attempt
            attempt = Attempt.objects.create(
                user=user,
                exercise=exercise,
                passed=passed,
                score=score,
                attempt_data=attempt_data
            )
            
            # Award XP if passed for the first time
            if passed and not exercise.attempts.filter(user=user, passed=True).exclude(pk=attempt.pk).exists():
                user.add_xp(exercise.xp_reward)
                
                # Check for badges and achievements
                from gamification.models import Badge, Achievement
                
                # Check badges
                for badge in Badge.objects.filter(is_active=True):
                    badge.check_and_award(user)
                
                xp_awarded = exercise.xp_reward
            else:
                xp_awarded = 0
            
            return JsonResponse({
                'success': True,
                'passed': passed,
                'score': score,
                'xp_awarded': xp_awarded,
                'total_xp': user.xp,
                'level': user.level
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class UseHintView(LoginRequiredMixin, View):
    """Use a hint (AJAX endpoint)"""
    
    def post(self, request, pk):
        try:
            hint = get_object_or_404(Hint, pk=pk)
            user = request.user
            
            # Check if already used
            if HintUsage.objects.filter(user=user, hint=hint).exists():
                return JsonResponse({
                    'success': True,
                    'content': hint.content,
                    'already_used': True
                })
            
            # Create usage record
            HintUsage.objects.create(user=user, hint=hint)
            
            # Deduct XP if cost > 0
            if hint.xp_cost > 0:
                user.xp = max(0, user.xp - hint.xp_cost)
                user.save()
            
            return JsonResponse({
                'success': True,
                'content': hint.content,
                'xp_cost': hint.xp_cost,
                'remaining_xp': user.xp
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)


class AttemptListView(LoginRequiredMixin, ListView):
    """List user's attempts"""
    model = Attempt
    template_name = 'exercises/attempt_list.html'
    context_object_name = 'attempts'
    paginate_by = 20
    
    def get_queryset(self):
        return Attempt.objects.filter(user=self.request.user).select_related('exercise__chapter')
