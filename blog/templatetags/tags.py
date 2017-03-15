from django import template 
from datetime import *
from django.template.defaultfilters import stringfilter


register = template.Library()



@register.simple_tag
@register.filter
@stringfilter
def nights():
    today = date.today()
    future = date(2058,2,16)
    nights = (future-today).days
    # nights = '{:.{prec}f}'.format(nights, prec=0)
    nights = '{:,}'.format(nights)

    return nights

nights.is_safe = True