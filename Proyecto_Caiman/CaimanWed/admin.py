from django.contrib import admin
from .models import Usuario

# En la tabla de la DB muetra por categoria los datos
class AdmUsuario(admin.ModelAdmin):
    list_display=['rut','nombre','apellido','email']

    # Filtra la tabla por apellido
    list_filter=['apellido']

# Register your models here.
admin.site.register(Usuario, AdmUsuario)