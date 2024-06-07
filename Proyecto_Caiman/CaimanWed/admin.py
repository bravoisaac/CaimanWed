from django.contrib import admin
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

# Registra tus modelos aquí

admin.site.register(Producto)
admin.site.register(Transportista)
admin.site.register(OrdenDespacho)
admin.site.register(DetalleOrden)
admin.site.register(Supermercado)
admin.site.register(Envio)
admin.site.register(Usuario)
