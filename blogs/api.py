# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from rest_framework.viewsets import ModelViewSet

class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    def get_serializer_class(self):
        return BlogSerializer

