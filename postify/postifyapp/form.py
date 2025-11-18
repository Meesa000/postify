from django import forms
from django.forms import ModelForm
from .models import PostForm

class PostForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ['author', 'message']
            