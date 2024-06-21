from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
