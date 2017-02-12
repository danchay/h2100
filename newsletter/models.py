from django.db import models

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	# auto_now_add is when the model is created; auto_now is at any time whatever; so this is only done once
	# an updated field would be almost the same, but reversed
	# blank in the form, null in the database

	def __str__(self):
		return self.email

