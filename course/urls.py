from django.urls import path, include
from rest_framework.routers import SimpleRouter

from course import views


router = SimpleRouter()
router.register(r'', views.CourseViewSet, basename='course')

urlpatterns = [
    path('subject/', views.SubjectCreateListView.as_view(), name='subject-list'),
    path('search/', views.CourseSearchView.as_view()),
    # http://127.0.0.1:8000/api/v1/course/<id>/review/
    # http://127.0.0.1:8000/api/v1/course/id/like/

] + router.urls     # only plus! not include (everything can break down!)
