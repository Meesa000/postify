from django import forms

class PostForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username:")
    post_area = forms.CharField(widget=forms.Textarea, label="Your Post:")