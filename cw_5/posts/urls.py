from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('login/auth/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('posts/', views.posts_list, name='posts'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
]
