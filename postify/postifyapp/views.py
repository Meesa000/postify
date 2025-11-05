from django.shortcuts import render

# Create your views here.
def homepage(request):
    posts = {"post1" : "I guess this is where a random post will appear? It would probably "
             "be good to have this in the center, similar to twitter."}
    
    return render(request, "index.html", posts)