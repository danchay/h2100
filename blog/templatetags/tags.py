from django import template 
from datetime import *

register = template.Library()

@register.simple_tag
def nights():
	today = date.today()
	future = date(2058,2,16)
	nights = (future-today).days
	# nights = '{:.{prec}f}'.format(nights, prec=0)
	nights = '{:,}'.format(nights)

	return nights
