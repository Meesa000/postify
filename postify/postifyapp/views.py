from django.shortcuts import render
from .models import PostForm as PostFormDB
from .form import PostForm
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    
    posts = {
        
            "posts" : PostFormDB.objects.all()}
 
    context = {
        **posts
    }

    return render(request, "index.html", context)

