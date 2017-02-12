from django.conf.urls import url
# from blog import views better done as below to avoid multiple view calls if app
# is added to other projects.
from contact.views import contact

urlpatterns = [
   url(r'^$', contact, name='contact'),
   # url(r'^add_post/', add_post, name='add_post)'),    
   # url(r'^(?P<slug>[\w|\-]+)/$', post, name='post'),
]

