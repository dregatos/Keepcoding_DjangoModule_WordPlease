# -*- coding: utf-8 -*-
from rest_framework import serializers
from blogs.models import Blog, Post


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        read_only_fields = ('owner',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('blog',)

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'summary', 'image_url', 'publication_date')