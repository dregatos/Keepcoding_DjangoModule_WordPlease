from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls
from blogs import urls as blogs_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

     #Users URLs
    url(r'', include(users_urls)),

     #Blogs URLs
    url(r'', include(blogs_urls)),
]
