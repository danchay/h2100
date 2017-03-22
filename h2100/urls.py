

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite
AdminSite.site_header = 'Hacking To 100: '
AdminSite.site_title = 'Hacking To 100'
AdminSite.index_title = 'H2100 Apps Admin'


from .settings import MEDIA_URL
from .settings import STATIC_URL, STATIC_ROOT
from .views import * 
from blog import views as blog_views

 




urlpatterns = [
    url(r'^about-this-site/$', about, name='about'),
    url(r'^$', blog_views.index, name="index"),
    url(r'^index/', blog_views.index),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^backend/', include(admin.site.urls)),
    url(r'^ckwotes/', include('ckwotes.urls', namespace='ckwotes')),
    # url(r'^about/', views.about, name="about"),

] 


if settings.DEBUG:
    from .settings import MEDIA_ROOT
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler400 = 'h2100.views.bad_request'
handler403 = 'h2100.views.permission_denied'
handler404 = 'h2100.views.page_not_found'
handler500 = 'h2100.views.server_error'
