from django.urls import path
from .import views



path('login/', views.login, name='custom_login'),