from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.login, name='login'),
    path('password', views.password, name='password'),
    path('register', views.register, name='register'),
]
