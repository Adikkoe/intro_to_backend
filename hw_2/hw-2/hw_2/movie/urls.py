from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list, name='movie-list'),
    path('<int:id>/', movie_detail, name='movie-detail'),
]

