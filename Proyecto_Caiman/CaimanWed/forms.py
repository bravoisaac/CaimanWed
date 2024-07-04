from django.contrib.auth.forms import AuthenticationForm
from .models import  Usuario, Producto
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'tipo']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'tipo']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'categoria', 'stock')
