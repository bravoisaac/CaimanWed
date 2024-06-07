from django.shortcuts import render
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

def index(request):
    return render(request, 'index.html')



def reporte_inventario(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'reporte_inventario.html', {'productos': productos})

# Define otras vistas según tus necesidades
