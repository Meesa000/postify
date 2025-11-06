from django.shortcuts import render
from .form import PostForm

# Create your views here.
def homepage(request):

    username = {"username" : ["User1", "User2", "User3", "User4", "User5"]}
    posts = {
        
            "posts" : ["I guess this is where a random post will appear? It would probably "
             "be good to have this in the center, similar to twitter.",
             "Another post! Wow, so much content.",
             "Django is really cool for web development.",
             "I love coding in Python!",
             "This is a sample post for the Postify app.",
             "Just another post to fill up space.",
             "Learning new things every day!",
             "Web development is fun!",
             "Hope you're enjoying Postify!",
             "Last post in the list."]}
    form = PostForm()
    context = {
        **posts, **username, **{"form": form}
    }

    
    return render(request, "index.html", context)

