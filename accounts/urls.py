from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registration
    path('register/student/', views.StudentRegistrationView.as_view(), name='student_register'),
    path('register/teacher/', views.TeacherRegistrationView.as_view(), name='teacher_register'),
    
    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    # Classroom management
    path('classroom/create/', views.ClassroomCreateView.as_view(), name='classroom_create'),
    path('classroom/<int:pk>/', views.ClassroomDetailView.as_view(), name='classroom_detail'),
    path('classroom/join/', views.JoinClassroomView.as_view(), name='classroom_join'),
    path('classroom/<int:pk>/leave/', views.LeaveClassroomView.as_view(), name='classroom_leave'),
]
