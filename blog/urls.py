from django.conf.urls import url

from blog.views import (
		index,
		post,
		healthspan,
		training,
		eating,
		sleeping,
		learning,
		other,
	)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^healthspan/$', healthspan, name='healthspan'), 
	url(r'^training/$', training, name='training'),  
	url(r'^eating/$', eating, name='eating'), 
	url(r'^sleeping/$', sleeping, name='sleeping'), 
	url(r'^learning/$', learning, name='learning'),   
	url(r'^other/$', other, name='other'), 
    url(r'^(?P<slug>[\w|\-]+)/$', post, name='post'),    
]
	# url(r'^add_post/$', add_post, name='add_post'),
	# url(r'^(?P<slug>[\w|\-]+)/edit/$', update_post, name="edit"),	
	# url(r'^(?P<slug>[\w|\-]+)/delete/$', delete_post),  
	# url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
	# url(r'^healthspan/$', healthspan, name='healthspan'), 
	# url(r'^training/$', training, name='training'),  
	# url(r'^eating/$', eating, name='eating'), 
	# url(r'^sleeping/$', sleeping, name='sleeping'), 
	# url(r'^learning/$', learning, name='learning'),   
	# url(r'^other/$', other, name='other'),  
	# url(r'^(?P<slug>[\w|\-]+)/$', post, name='post'),

