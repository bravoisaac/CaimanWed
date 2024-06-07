from django.urls import path
from .views import reporte_inventario

urlpatterns = [
    path('reporte_inventario/', reporte_inventario, name='reporte_inventario'),
    # Otras URLs de tu aplicación
]
