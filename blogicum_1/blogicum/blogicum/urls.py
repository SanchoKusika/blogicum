from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', include('blog.urls')),  # Маршруты из приложения blog
    path('pages/', include('pages.urls')),  # Маршруты из приложения pages
]
