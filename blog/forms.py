from django import forms 
from blog.models import Post 

from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	preview = forms.CharField(widget=PagedownWidget(show_preview=False))
	body_text = forms.CharField(widget=PagedownWidget(show_preview=False))

	class Meta:
		model = Post 
		fields = [
			'title', 
			'preview', 
			'body_text', 
			'image', 
			'category', 
			'tag', 
			'status'
		] 