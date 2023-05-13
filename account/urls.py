from django.contrib import admin
from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginViewVerm.as_view(), name='login'),
    path('sign_in/', sign_in, name='sign_in'), # Функция входа
    path('logout/', unlogin, name='logout'),
]