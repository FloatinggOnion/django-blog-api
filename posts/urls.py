from django.urls import path
from .views import ListPosts, DetailPosts

urlpatterns = [
    path('', ListPosts.as_view()),
    path('<int:pk>/', DetailPosts.as_view()),
]