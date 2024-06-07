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
    

