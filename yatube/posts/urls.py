from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='homepage'),
    # Страница группы
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
