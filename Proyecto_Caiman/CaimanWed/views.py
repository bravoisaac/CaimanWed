from django.shortcuts import render
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

def index(request):
    return render(request, 'index.html')

# Define otras vistas según tus necesidades
