from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Course list
    path('', views.CourseListView.as_view(), name='course_list'),

    # Course detail
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),

    # Chapter detail
    path('<str:course_slug>/<slug:chapter_slug>/', views.ChapterDetailView.as_view(), name='chapter_detail'),

    # Chapter assignment (for teachers)
    path('chapter/<int:pk>/assign/', views.AssignChapterView.as_view(), name='assign_chapter'),
]