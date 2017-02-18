from django.shortcuts import render

from django.shortcuts import get_object_or_404, render_to_response, redirect 

from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.core.mail import send_mail


from .forms import SignUpForm

# from blog.models import Post 
# from blog.forms import PostForm

# def index(request):
# 	t = loader.get_template('newsletter/index.html')
# 	context_dict = { 'entry': 'Hello Woorld.'}
# 	return HttpResponse(t.render(context_dict))

def newsletter(request):
	title = "Newsletter"
	# if request.user.is_authenticated():
	# 	title = "Newsletter: %s" %(request.user)
	# if request.method == "POST":
	# 	print(request.POST) Not recommended. Should used cleaned_data.get()

	form = SignUpForm(request.POST or None)


	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Anonymous"
		# if not instance.full_name:
		# 	instance.full_name = "Anonymous"
		instance.save() 
		print(instance.email + str(instance.timestamp))

	if form.is_valid():
		context = {
			"template_title": "Thank you"
		}
	else:
		context = {
			"template_title": title,
			"form": form
		}

	return render(request, "newsletter/index.html", context)

def contact(request):
	send_mail(
	    'Subject here',
	    'Here is the message.',
	    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
	)	