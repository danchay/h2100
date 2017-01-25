from django import forms 

from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
	url = forms.CharField(
		label='', 
		validators=[validate_url],
		widget = forms.TextInput(
				attrs = {
					"placeholder": "Long URL",
					"class": "form-control"
					}
			)
		)


# Move these helper function to their own module
# def validate_url(value):
# 	url_validator = URLValidator()		
# 	try:
# 		url_validator(value)
# 	except:
# 		raise forms.ValidationError("Invalid URL for this field")
# 	return value	

# def validate_dot_com(value):
# 	if not "com" in value:
# 		raise ValidationError("This is not a .com address.")	

# class SubmitUrlForm(forms.Form):
# 	url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])



	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean()
	# 	#print(cleaned_data)
	# 	# This clean() method is called every time the views'
	# 	# form.is_valid() method is called.
	# 	# url=cleaned_data.get("url")
	# 	print(cleaned_data)
	# 	url=cleaned_data.get('url')
	# 	url_validator = URLValidator()		
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL for this field")

	# 	return url
	# 	# url=cleaned_data['url']
	# 	# print("Form: " + url)

	# The clean_url only validates the field
	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	if "http://" in url:
	# 		return url
	# 	return 'http://' + url


		# if not "com" in url:
		# 	raise forms.ValidationError("This is not a .com address.")
		# # print("This: " + url)
		# url_validator = URLValidator()
		# try:
		# 	url_validator(url)
		# except:
		# 	raise forms.ValidationError("Invalid URL for this field")

		# return url


'''
Validate 1) the entire form, 2) the fields in particular, 3) custom validation for 
form field or model field. 
'''