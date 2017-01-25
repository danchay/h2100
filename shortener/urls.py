from django.conf.urls import url
from shortener.views import  URLRedirectView, HomeView


urlpatterns = [
	url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
]

# Note the .as_view() function call needed in the class-based view
# The redirect urls should be last in the list of urls
# url(r'^a/(?P<shortcode>[\w-]+){6,15}/$', shurl_redirect_view),
# url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', ShurlCBView.as_view()),
# These urls are achieved with /shortener/