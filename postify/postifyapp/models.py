from django.db import models


class PostForm(models.Model):
    author = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return f"Author: {self.author} Message: {self.message}"  