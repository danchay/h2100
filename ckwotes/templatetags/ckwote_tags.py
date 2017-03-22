from django import template 
from ckwotes.models import Ckwote 
from blog.models import Category

from random import shuffle

register = template.Library()

@register.simple_tag 
def ckwote():
	quote_list = list(Ckwote.objects.all().filter(status='p'))

	shuffle(quote_list)

	
	if not quote_list:
		ckwote=''
	else:
		ckwote=quote_list[0]

	return ckwote

