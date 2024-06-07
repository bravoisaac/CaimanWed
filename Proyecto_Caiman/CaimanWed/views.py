from django.shortcuts import render
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

def index(request):
    return render(request, 'index.html')



def reporte_inventario(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'reporte_inventario.html', {'productos': productos})

# Define otras vistas según tus necesidades
from django.shortcuts import render,redirect
from .forms import RegistroForm
# Create your views here.

def registro(request):   
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('index') 
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
    

def index(request):
    return render (request,'index.html')