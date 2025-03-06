from django.contrib import admin
from .models import User, Table, Reservation

# Модельдерді Django Admin-ге қосу
admin.site.register(User)
admin.site.register(Table)
admin.site.register(Reservation)
