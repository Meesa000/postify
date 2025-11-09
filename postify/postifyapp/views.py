from django.shortcuts import render
from .form import PostForm

# Create your views here.
def homepage(request):

    username = {"username" : ["User1", "User2", "User3", "User4", "User5"]}
    posts = {
        
            "posts" : []}

    post_form = PostForm(request.POST)
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
        
        
    context = {
        **posts, **username, **{"post_form": post_form}
    }

    return render(request, "index.html", context)

