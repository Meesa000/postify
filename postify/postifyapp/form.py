from django import forms
from django.forms import ModelForm
from .models import PostForm

class PostForm(ModelForm):
    author = forms.TextInput()
    message = forms.TextInput()
    
    class Meta:
        model = PostForm
        fields = ['author', 'message']
        