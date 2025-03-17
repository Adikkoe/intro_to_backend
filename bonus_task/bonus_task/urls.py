from django.contrib import admin
from django.urls import path, include
from note.views import home  # Этот импорт должен работать

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('notes/', include('note.urls')),
]
