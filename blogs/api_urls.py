# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from blogs.api import BlogViewSet
from rest_framework.routers import DefaultRouter


# APIRouter
router = DefaultRouter()
router.register(r'blogs', BlogViewSet)


urlpatterns = [
    # API URLs
    url(r'1.0/', include(router.urls)),  # incluyo las URLS de API
]