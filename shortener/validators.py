from django.core.exceptions import ValidationError 
from django.core.validators import URLValidator 

def validate_url(value):
	url_validator = URLValidator()	

	reg_value = value 
	if "http" in reg_value:
		new_value = reg_value 
	else:
		new_value = 'http://' + value 
	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalid URL for this field")
	return new_value

	# value_1 = True
	# value_2 = True

	# try:
	# 	url_validator(value)
	# except:
	# 	value_1 = False

	# value_2_url = "http://" + value

	# try:
	# 	url_validator(value_2_url)
	# except:
	# 	value_2 = False

	# if value_1 == False and value_2 == False:
	# 	raise ValidationError("Invalid URL for this field")
	# return value	

def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("This is not a .com address.")