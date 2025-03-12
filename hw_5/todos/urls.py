from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('login/auth/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('todos/', views.todos_list, name='todos'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]
