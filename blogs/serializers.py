# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import serializers
from blogs.models import Blog, Post

class BlogSerializer(serializers.ModelSerializer):

    # añado estos parámetros al return
    blog_url = serializers.SerializerMethodField('blogUrl')

    class Meta:
        model = Blog
        read_only_fields = ('owner',)
        fields = ('name', 'owner', 'blog_url')

    def blogUrl(self, obj):
        return reverse('blog_detail', kwargs={'username': obj.owner.username})

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('blog',)

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'summary', 'image_url', 'publication_date')