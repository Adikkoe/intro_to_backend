from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
]
