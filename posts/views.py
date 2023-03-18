from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import Post
from rest_framework import generics, viewsets
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    