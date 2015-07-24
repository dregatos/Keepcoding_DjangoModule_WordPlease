# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blogs.models import Blog, Post
from blogs.serializers import BlogSerializer, PostListSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet
from blogs.views import PostsQueryset


class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BlogSerializer

class PostViewSet(PostsQueryset, ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_posts_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        #obtener blog del usuario y asignarlo
        user_blog = Blog.objects.get(owner=self.request.user)
        serializer.save(blog=user_blog)
