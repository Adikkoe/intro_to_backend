from django.contrib import admin
from django.urls import path
from mt import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin панелі
    path('', views.home, name='home'),  # Басты бет

    # Пайдаланушылар
    path('users/', views.users_list, name='users_list'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),

    # Үстелдер
    path('tables/', views.tables_list, name='tables_list'),
    path('tables/create/', views.create_table, name='create_table'),

    # Броньдар
    path('reservations/create/', views.create_reservation, name='create_reservation'),
    path('reservations/<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/<int:id>/update/', views.update_reservation_status, name='update_reservation_status'),
]
