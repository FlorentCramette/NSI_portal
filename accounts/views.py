from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, TemplateView, FormView, View
from django.urls import reverse_lazy
from .models import User, Classroom, Enrollment
from .forms import StudentRegistrationForm, TeacherRegistrationForm, JoinClassroomForm, ClassroomCreateForm


class StudentRegistrationView(CreateView):
    """Student registration view"""
    model = User
    form_class = StudentRegistrationForm
    template_name = 'accounts/student_register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Compte créé avec succès ! Vous pouvez maintenant vous connecter.')
        return response


class TeacherRegistrationView(CreateView):
    """Teacher registration view"""
    model = User
    form_class = TeacherRegistrationForm
    template_name = 'accounts/teacher_register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Compte professeur créé avec succès ! Vous pouvez maintenant vous connecter.')
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    """User profile view"""
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context['user'] = user
        
        if user.is_student:
            context['classrooms'] = Classroom.objects.filter(enrollments__user=user)
            context['total_attempts'] = user.attempts.count()
            context['passed_exercises'] = user.attempts.filter(passed=True).values('exercise').distinct().count()
        elif user.is_teacher:
            context['classrooms'] = user.classrooms_taught.all()
        
        return context


class ClassroomCreateView(LoginRequiredMixin, CreateView):
    """Teacher creates a classroom"""
    model = Classroom
    form_class = ClassroomCreateForm
    template_name = 'accounts/classroom_create.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Classe créée avec succès ! Code : {form.instance.join_code}')
        return response
    
    def get_success_url(self):
        return reverse_lazy('accounts:classroom_detail', kwargs={'pk': self.object.pk})


class ClassroomDetailView(LoginRequiredMixin, DetailView):
    """View classroom details and students"""
    model = Classroom
    template_name = 'accounts/classroom_detail.html'
    context_object_name = 'classroom'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classroom = self.object
        
        # Get students with their stats
        students = []
        for enrollment in classroom.enrollments.select_related('user'):
            student = enrollment.user
            students.append({
                'user': student,
                'total_xp': student.xp,
                'level': student.level,
                'exercises_passed': student.attempts.filter(passed=True).values('exercise').distinct().count(),
            })
        
        context['students'] = students
        context['is_teacher'] = self.request.user == classroom.teacher
        
        return context


class JoinClassroomView(LoginRequiredMixin, FormView):
    """Student joins a classroom"""
    form_class = JoinClassroomForm
    template_name = 'accounts/join_classroom.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        join_code = form.cleaned_data['join_code']
        classroom = get_object_or_404(Classroom, join_code=join_code)
        
        # Check if already enrolled
        if Enrollment.objects.filter(user=self.request.user, classroom=classroom).exists():
            messages.warning(self.request, 'Vous êtes déjà inscrit dans cette classe.')
        else:
            Enrollment.objects.create(user=self.request.user, classroom=classroom)
            messages.success(self.request, f'Vous avez rejoint la classe {classroom.name} !')
        
        return super().form_valid(form)


class LeaveClassroomView(LoginRequiredMixin, View):
    """Student leaves a classroom"""
    
    def post(self, request, pk):
        classroom = get_object_or_404(Classroom, pk=pk)
        enrollment = get_object_or_404(Enrollment, user=request.user, classroom=classroom)
        enrollment.delete()
        messages.success(request, f'Vous avez quitté la classe {classroom.name}.')
        return redirect('dashboard')
