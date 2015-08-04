# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogSerializer, PostListSerializer, PostSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from blogs.views import PostsQueryset
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogViewSet(ReadOnlyModelViewSet):

    queryset = Blog.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('owner__username')
    ordering_fields = ('name')

    def get_serializer_class(self):
        return BlogSerializer

class PostViewSet(PostsQueryset, ModelViewSet):

    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (PostPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'summary', 'text')
    ordering_fields = ('title', 'publication_date')

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
