from django.shortcuts import render
from .form import PostForm

# Create your views here.
def homepage(request):

    username = {"username" : ["User1", "User2", "User3", "User4", "User5"]}
    posts = {
        
            "posts" : [""]}

    post_form= PostForm()

    # Handle post submission form
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            print("Post submitted!")
            author = post_form.cleaned_data["username"]
            message = post_form.cleaned_data["post_area"]
            print(f"Message: {message} was posted by: {author}")
            posts["posts"].insert(len(posts["posts"]), f"{author}: {message}")
            print(posts["posts"])
        else:
            post_form = PostForm()
        
    context = {
        **posts, **username, **{"post_form": post_form}
    }

    return render(request, "index.html", context)

