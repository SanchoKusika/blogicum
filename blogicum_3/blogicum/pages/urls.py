from django.urls import path
from . import views

app_name = 'pages'  # Указываем namespace для приложения pages

urlpatterns = [
    path('about/', views.about, name='about'),  # Страница "О проекте"
    path('rules/', views.rules, name='rules'),  # Страница "Наши правила"
]
