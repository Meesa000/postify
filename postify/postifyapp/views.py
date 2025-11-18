from django.shortcuts import render
from .models import PostForm as PostFormModel
from .form import PostForm
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm()

    posts = {"posts": PostFormModel.objects.all()}
    context = {"post_form": post_form, **posts}

    return render(request, "index.html", context)

