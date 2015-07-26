# -*- coding: utf-8 -*-
from datetime import date
from django.core.urlresolvers import reverse
from rest_framework import serializers
from blogs.models import Blog, Post

class BlogSerializer(serializers.ModelSerializer):

    # añado estos parámetros al return
    blog_url = serializers.SerializerMethodField('blogUrl')
    published_posts_count = serializers.SerializerMethodField('publishedPostsCount')

    class Meta:
        model = Blog
        read_only_fields = ('owner',)
        fields = ('name', 'owner', 'blog_url', 'published_posts_count')

    def blogUrl(self, obj):
        return reverse('blog_detail', kwargs={'username': obj.owner.username})

    def publishedPostsCount(self, obj):
        return len(Post.objects.filter(blog=obj, publication_date__lte=date.today))

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('blog',)

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'summary', 'image_url', 'publication_date')