from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/create/', views.post_create_view, name='post_create'),
]
