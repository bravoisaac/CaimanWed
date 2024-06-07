from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  Usuario

class UsuarioForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']