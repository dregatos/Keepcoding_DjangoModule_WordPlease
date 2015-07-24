# -*- coding: utf-8 -*-
from rest_framework import serializers
from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        read_only_fields = ('owner',)