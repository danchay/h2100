from django.conf.urls import url
# from blog import views better done as below to avoid multiple view calls if app
# is added to other projects.
from blog.views import index, add_post, post, training, healthspan, eating, sleeping, learning, other

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_post/$', add_post, name='add_post'),
	url(r'^healthspan/$', healthspan, name='healthspan'), 
	url(r'^training/$', training, name='training'),  
	url(r'^eating/$', eating, name='eating'), 
	url(r'^sleeping/$', sleeping, name='sleeping'), 
	url(r'^learning/$', learning, name='learning'),   
	url(r'^other/$', other, name='other'),  
	url(r'^(?P<slug>[\w|\-]+)/$', post, name='post'),  
]