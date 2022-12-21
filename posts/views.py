from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class ListPosts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPosts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )