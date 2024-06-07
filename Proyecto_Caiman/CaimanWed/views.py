from django.shortcuts import render
from .models import Usuario
from django.shortcuts import get_object_or_404

# Create your views here.

def usuarios(request):
    user=Usuario.objects.all()
    datos={
        "usuarios":user
    }
    return render(request, 'CaimanWed/usuarios.html', datos)


def detalleusuario(request,id):
    usuarios=get_object_or_404(Usuario, rut= id)

    datos={
        "usuarios":usuarios
    }
    return render(request,'Caiman/detalleusuario.html', datos)