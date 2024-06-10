from django.shortcuts import render,redirect
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')
from .forms import UsuarioForm
def index(request):
    return render(request, 'index.html')


def reporte_inventario(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'reporte_inventario.html', {'productos': productos})

# Define otras vistas según tus necesidades


# Create your views here.

def registro(request):   
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('store') 
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detalle.html', {'producto': producto})

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_detalle', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto_editar.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_detalle', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_editar.html', {'form': form})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('producto_list')

    

