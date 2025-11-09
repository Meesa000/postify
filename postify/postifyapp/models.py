from django.db import models

class PostForm(models.Model):
    author = models.CharField(max_length=20)
    message = models.CharField(max_length=200)