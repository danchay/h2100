from django.conf import settings
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render_to_response, redirect 
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.core.mail import send_mail

from .forms import ContactForm
from django.core.mail import send_mail




def contact(request):
	title = "Send Me a Message"
	form = ContactForm(request.POST or None)
	form_email = ''
	form_full_name = ''
	form_message = ''

	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		# print(form_email)
	subject = 'H2100 contact form'
	from_email = settings.EMAIL_HOST_USER 
	to_email = [from_email, 'danchay@gmail.com']
	contact_message = "%s via %s -- Message: %s" % (
		form_full_name,
		form_email, 
		form_message 
		)

	send_mail(subject, 
		contact_message, 
		from_email, 
		to_email, 
		fail_silently=False)

	if form_email:
		context = {
			'title': "Message sent. Thank you." 
			}
	else:
		context = {
			'title': title,
			'form': form
		}


	return render(request, "contact/index.html", context)


