from urllib import parse 
from django import template 

register = template.Library()


####################################################
# Example:                                         #
# share_string = parse.quote(instance.header_text) #
####################################################

@register.filter
def urlify(value):
	return parse.quote(value)