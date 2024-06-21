from django.contrib import admin
from .models import Usuario

# En la tabla de la DB muetra por categoria los datos
class AdmUsuario(admin.ModelAdmin):
    list_display=['nombre','email','contrasena','tipo']

    # Filtra la tabla por apellido
    list_filter=['nombre']

# Register your models here.
admin.site.register(Usuario, AdmUsuario)