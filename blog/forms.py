from django import forms 
from blog.models import Post 

from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	header_text = forms.CharField(widget=PagedownWidget)
	body_text = forms.CharField(widget=PagedownWidget)

	class Meta:
		model = Post 
		fields = ['title', 'header_text', 'body_text', 'image', 'category', 'tag', 'status'] 