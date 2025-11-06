from django import forms

class PostForm(forms.Form):
    post_area = forms.CharField(widget=forms.Textarea, label="Your Post:")