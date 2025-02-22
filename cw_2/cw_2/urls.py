from django.contrib import admin
from django.urls import path, include
from post.views import post_list_view  # import your view for the root path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list_view, name='home'),  # add this line to handle the root path
    path('posts/', include('post.urls')),
]
