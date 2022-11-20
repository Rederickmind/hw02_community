# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        # Шаблон, для отображения возвращаемой страницы.
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    # Полный адрес страницы регистрации - auth/signup/,
    path('signup/', views.SignUp.as_view(), name='signup')
]
