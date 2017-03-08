from django import forms 
from blog.models import Post 

class PostForm(forms.ModelForm):

	class Meta:
		model = Post 
		fields = ['title', 'header_text', 'body_text', 'image', 'category', 'tag', 'status'] 