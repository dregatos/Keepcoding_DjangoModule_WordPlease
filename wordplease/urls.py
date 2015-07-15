from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

     #Users URLs
    url(r'', include(users_urls))
]
