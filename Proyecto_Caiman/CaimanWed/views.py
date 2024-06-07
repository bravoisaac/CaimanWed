from django.shortcuts import render,redirect
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario

from django.shortcuts import render, redirect
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
def index(request):
    return render(request, 'index.html')

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

def login(request):
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('email')  
            password = formulario.cleaned_data.get('contrasena')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.rol:
                    return redirect('home')
                else:
                    return redirect('login/')
    else:
        formulario = UsuarioForm()
        
    return render(request, 'login/login.html', {'formulario': formulario})


def registro(request):   
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('store') 
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})
    