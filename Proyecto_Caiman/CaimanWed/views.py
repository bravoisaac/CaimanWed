from django.shortcuts import render
from datetime import date
from .models import Usuario
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index_prueba(request):
    fecha=date.isoformat(date.today())
    texto="Paa traer los datos desde la vista se debe enviar a través del contenido de contexto"
    lista=['Alfajor','Poleron','Paraguas','Gorro','Guz con Microfono']
    elementos=len(lista)

    datos={
        "fecha":fecha,
        "msg":texto,
        "lista":lista,
        "items":elementos
    }


    return render(request,'CaimanWed/index_prueba.html', datos)


def usuarios(request):
    user=Usuario.objects.all()
    
    datos={
        "usuarios":user
    }
    return render(request, 'CaimanWed/usuarios.html', datos)


def detalleusuario(request, id):
    usuario=get_object_or_404(Usuario, nombre= id)

    datos={
        "usuario":usuario
    }
    return render(request,'CaimanWed/detalleusuario.html', datos)



def modificar_usuario(request, id):
    usuario=get_object_or_404(Usuario, nombre= id)


    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="usuarios")
        
    datos={

        "usuario":usuario
    }

    return render(request,'CaimanWed/modificar_usuario.html', datos)



def eliminar_usuario(request, id):
    usuario=get_object_or_404(Usuario, nombre= id)
    
    if request.method=="POST":

        usuario.delete()
        return redirect(to="usuarios")
    
    datos={
        "usuario":usuario
    }


    return render(request, 'CaimanWed/eliminar_usuario.html', datos)