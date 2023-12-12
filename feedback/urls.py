from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('review', views.ReviewViewSet)

urlpatterns = [
    # path('', include(router.urls)),

    path('like/', views.LikeCreateView.as_view()),
    path('like/<int:pk>/', views.LikeDeleteView.as_view()),
    path('user/like/', views.UserLikesView.as_view()),
]
