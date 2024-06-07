from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='custom_login'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
]
