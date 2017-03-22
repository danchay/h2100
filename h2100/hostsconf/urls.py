from django.conf.urls import url, include
from django.contrib import admin
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),

]
