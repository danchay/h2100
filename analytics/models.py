from django.db import models

from shortener.models import ShURL


class ClickEventManager(models.Manager):
	def create_event(self, shurl_instance):
		if isinstance(shurl_instance, ShURL ):
			obj, created = self.get_or_create(shurl=shurl_instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	shurl 		= models.OneToOneField(ShURL)
	count 		= models.IntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True) 
	timestamp	=models.DateTimeField(auto_now_add=True) 

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)


