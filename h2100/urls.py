"""h2100 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .settings import MEDIA_URL
from .settings import STATIC_URL, STATIC_ROOT


urlpatterns = [
    url(r'^$', include('blog.urls')),
    url(r'^backend/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^shortener/', include('shortener.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^contact/', include('contact.urls')),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
] 

if settings.DEBUG:
    from .settings import MEDIA_ROOT
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
