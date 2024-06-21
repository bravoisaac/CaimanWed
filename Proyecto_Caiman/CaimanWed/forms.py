from django import forms
from .models import Producto
from .models import Usuario

class UsuarioForm(forms.ModelForm):
from django.contrib.auth.forms import AuthenticationForm
from .models import  Usuario

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'tipo']

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'categoria', 'stock')
        fields = ['email', 'contrasena','contrasena', 'tipo']