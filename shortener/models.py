from django.conf import settings
from django.db import models

#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
from .validators import validate_url, validate_dot_com
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShURLManager(models.Manager):

	def all(self, *args, **kwargs):
		qs_main = super(ShURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):
		qs = ShURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(str(q.id) + ": " + q.shortcode)
			q.save()
			new_codes+=1
		return "New codes made: {i}".format(i=new_codes)
	# This kind of Management command like refresh_shortcodes can be useful 
	# for manipulating data.
	# isinstance() checks that variable is of class int

class ShURL(models.Model):
	url 		= models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True) # Required in db but not admin
	#shortcode 	= models.CharField(max_length=15, null=True) # Okay null in db
	#shortcode 	= models.CharField(max_length=15, default='defshtcode')
	updated 	= models.DateTimeField(auto_now=True) # On save
	timestamp	=models.DateTimeField(auto_now_add=True) # When created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False) #Set on our own
	active 		= models.BooleanField(default=True)

	objects = ShURLManager()

# python manage.py migrate Fake

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode=create_shortcode(self)
		if not "http" in self.url:
			self.url = "http://" + self.url
		super(ShURL, self).save(*args, **kwargs)

	# class Meta:
	# 	ordering = ('-id',)
	# If adding this meta, be sure to run migrations.

	def __str__(self):
		return str(self.url + ': ' + self.shortcode)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http', port='5000')
		# return "http://www.hackingto100.com/shortener/{shortcode}".format(shortcode=self.shortcode)
		return url_path
