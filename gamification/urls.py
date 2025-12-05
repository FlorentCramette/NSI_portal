from django.urls import path
from . import views

app_name = 'gamification'

urlpatterns = [
    # Badges
    path('badges/', views.BadgeListView.as_view(), name='badge_list'),
    
    # Leaderboard
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
]
