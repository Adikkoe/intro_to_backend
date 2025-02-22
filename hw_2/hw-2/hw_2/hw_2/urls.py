from django.contrib import admin
from django.urls import path, include  
from django.shortcuts import redirect  

def redirect_to_movies(request):
    return redirect('movie-list')  

urlpatterns = [
    path('', redirect_to_movies), 
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls')),
    path('articles/', include('blog.urls')),
]
