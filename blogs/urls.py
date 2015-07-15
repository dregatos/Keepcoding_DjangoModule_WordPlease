# -*- coding: utf-8 -*-

from django.conf.urls import url
from blogs.views import BlogListView, BlogDetailView, PostDetailView


urlpatterns = [
    #Blogs URLs
    url(r'^blogs/$', BlogListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[a-z0-9_-]{3,16})$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<username>[a-z0-9_-]{3,16})/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_detail')
]