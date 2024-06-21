from django.urls import path
from .views import index_prueba ,usuarios, detalleusuario, modificar_usuario, eliminar_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_prueba, name='index_prueba'),
    path('usuarios/', usuarios, name='usuarios'),
    path('detalleusuario/<id>', detalleusuario, name='detalleusuario'),
    path('modificar_usuario/<id>', modificar_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<id>', eliminar_usuario, name='eliminar_usuario')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)