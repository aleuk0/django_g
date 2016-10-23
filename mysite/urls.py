from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  #все запросы начинающиеся с admin будут отправляться на страницу admin'a
    url(r'', include('blog.urls')), #остальные запросы будут отправляться в приложение blog
]
