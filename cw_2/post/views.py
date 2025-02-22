from django.shortcuts import render
from .forms import PostForm
from .models import Post

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})
