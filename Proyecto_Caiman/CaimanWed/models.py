from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=3, null=False)
    apellido=models.CharField(max_length=4,null=False)
    email=models.EmailField(verbose_name="Correo electronico")
