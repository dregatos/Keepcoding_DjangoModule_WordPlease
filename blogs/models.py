# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.name

class Blog(models.Model):
    owner = models.OneToOneField(User)      # For now we DON'T ALLOW multiple blog per user
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=300)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True, null=True, default="")
    publication_date = models.DateField(default=date.today)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return u'%s' % (self.title)


