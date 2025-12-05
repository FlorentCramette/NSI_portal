from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
    # Exercise detail and execution
    path('<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    
    # Submit attempt (AJAX)
    path('<int:pk>/submit/', views.SubmitAttemptView.as_view(), name='submit_attempt'),
    
    # Get hint (AJAX)
    path('hint/<int:pk>/use/', views.UseHintView.as_view(), name='use_hint'),
    
    # User's attempts history
    path('attempts/', views.AttemptListView.as_view(), name='attempt_list'),
]
