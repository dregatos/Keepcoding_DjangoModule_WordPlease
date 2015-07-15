# -*- coding: utf-8 -*-

from django.conf.urls import url
from posts.views import HomeView,NewPostView


urlpatterns = [
    #Blogs URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),
    url(r'^new-post/$', NewPostView.as_view(), name='create_post'),

]
