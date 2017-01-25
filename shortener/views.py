from django.views.generic import View 

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from analytics.models import ClickEvent

from .models import ShURL
from .forms import SubmitUrlForm 


class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form=SubmitUrlForm()
		context= {
			"title": "H2100 URL_Shortener",
			"form": the_form,
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		# print(request.POST)
		# print(request.POST.get("url"))
		form = SubmitUrlForm(request.POST)
		context = { 
			"title": "H2100 URL_Shortener",
			"form": form,
		}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = ShURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request, template, context)


class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(ShURL, shortcode=shortcode) 
		# Save analytic data item
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)








'''
# Function based view
def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})

def shurl_redirect_view(request, shortcode=None, *args, **kwargs):
	obj = get_object_or_404(ShURL, shortcode=shortcode) 
	return HttpResponseRedirect(obj.url) 

def shurl_redirect_view(request, shortcode=None, *args, **kwargs):
	# print(args)
	# print(kwargs)
	# print(shortcode)
	# obj = ShURL.objects.get(shortcode=shortcode)
	# Or...#########################
	# try:
	# 	obj = ShURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj = ShURL.objects.all().first()
	# Or ... #######################
	# obj_url = None
	# qs = ShURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url
	# Or ... ########################
	obj = get_object_or_404(ShURL, shortcode=shortcode) 

	return HttpResponse("hello {sc}".format(sc=obj.url)) 

# A function based view will handle any method (GET, POST...) by default. 
# A class based view must have each method defined individually.
# Class based views are a bit more portable.

class ShurlCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		# print(args)
		# print(kwargs)
		# print(shortcode)
		obj = get_object_or_404(ShURL, shortcode=shortcode) 
		return HttpResponse("hello again {sc}".format(sc=shortcode))
'''