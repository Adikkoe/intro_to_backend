from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# 1. GET posts/
def posts_list(request):
    posts = Post.objects.all()
    posts_data = [{"id": post.id, "title": post.title, "author": post.author} for post in posts]
    return JsonResponse(posts_data, safe=False)

# 2. GET posts/:id
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post_data = {
        "id": post.id,
        "title": post.title,
        "description": post.description,
        "author": post.author
    }
    return JsonResponse(post_data)

# 3. POST posts/
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')  # Redirect to the list of posts
    else:
        form = PostForm()
    return render(request, 'post/post_create.html', {'form': form})

# 4. DELETE posts/:id/delete
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts_list')  # Redirect back to the posts list
