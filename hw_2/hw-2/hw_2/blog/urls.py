from django.urls import path
from . import views  # Импортируем ваши views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Пример маршрута для списка статей
    path('<int:id>/', views.article_detail, name='article_detail'),  # Пример маршрута для одной статьи
]
