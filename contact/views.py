from django.conf import settings
from django.core.mail import EmailMultiAlternatives, EmailMessage

from django.shortcuts import get_object_or_404, render_to_response, redirect, render 
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.template.loader import get_template
from django.core.mail import send_mail

from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    title = "Send Me a Message"
    contact_email = ''
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data.get("full_name", '')
            contact_email = form.cleaned_data.get("email", '')
            form_content = form.cleaned_data.get("message", '')

            template = get_template('contact/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                })
            content = template.render(context)
            print(content)

            from_email = settings.EMAIL_HOST_USER 

            email = EmailMessage(
                "H2100 contact form submission",
                content,
                "H2100" + '',
                [from_email,],
                headers = {'Reply-To': contact_email}
                )
            email.send()

    if contact_email:
        context = {
            'title': "Message sent. Thank you."           
        }
    else:
        context = {
            'title': title,
            'form': form_class
        }

    return render(request, 'contact/contact.html', context)



# def contact(request):
#   title = "Send Me a Message"
#   form = ContactForm(request.POST or None)
#   form_email = ''
#   form_full_name = ''
#   form_message = ''

#   if form.is_valid():
#       form_email = form.cleaned_data.get("email")
#       form_full_name = form.cleaned_data.get("full_name")
#       form_message = form.cleaned_data.get("message")
#       # print(form_email)
#   subject = 'H2100 contact form'
#   from_email = settings.EMAIL_HOST_USER 
#   to_email = [from_email, 'danchay@gmail.com']
#   contact_message = "%s via %s -- Message: %s" % (
#       form_full_name,
#       form_email, 
#       form_message 
#       )

#   html_message= '<strong>From:</strong> ' + form_full_name + '<br /><strong>Email:</strong> ' + form_email + '<br /><br /><strong>Message:</strong><br />' + form_message 

#   msg = EmailMultiAlternatives(subject, contact_message, from_email, to_email)
#   msg.attach_alternative(html_message, "text/html")
#   msg.send()

#   # send_mail( 
#   #   subject,
#   #   html_message,
#   #   from_email, 
#   #   to_email, 

#   #   fail_silently=False,
#   #   )

#   if form_email:
#       context = {
#           'title': "Message sent. Thank you." 
#           }
#   else:
#       context = {
#           'title': title,
#           'form': form
#       }


#   return render(request, "contact/contact.html", context)


