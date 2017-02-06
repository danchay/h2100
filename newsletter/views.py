from django.shortcuts import render

from django.shortcuts import get_object_or_404, render_to_response, redirect 

from django.http import HttpResponse
from django.template import Context, loader, RequestContext

# from blog.models import Post 
# from blog.forms import PostForm

def index(request):
	t = loader.get_template('newsletter/index.html')
	content = {'Hello Woorld.'}
	return HttpResponse(t.render(content))

