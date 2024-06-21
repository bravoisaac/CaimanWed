from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='custom_login'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),    
    path('registro/', views.registro, name='registro'),
    path('productolist', views.producto_list, name='producto_list'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('editar_producto/<int:pk>', views.producto_editar, name='producto_editar'),
    path('eliminar_producto/<int:pk>', views.producto_eliminar, name='producto_eliminar'),
     path('producto_nuevo/', views.producto_nuevo, name='producto_nuevo'),
]
