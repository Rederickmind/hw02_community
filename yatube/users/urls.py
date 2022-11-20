# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Страница регистрации - auth/signup/,
    path('signup/', views.SignUp.as_view(), name='signup'),
    # Страница выхода из учётной записи
    path(
        'logout/',
        # Шаблон, для отображения возвращаемой страницы.
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    # Страница входа в учётную запись
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
]
