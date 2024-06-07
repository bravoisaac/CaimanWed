from django.shortcuts import render, redirect
from .models import Producto, Transportista, OrdenDespacho, DetalleOrden, Supermercado, Envio, Usuario
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
def index(request):
    return render(request, 'index.html')


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
                    return redirect('login')
    else:
        formulario = UsuarioForm()
        
    return render(request, 'login/login.html', {'formulario': formulario})