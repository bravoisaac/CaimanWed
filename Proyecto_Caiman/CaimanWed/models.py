from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    categoria = models.CharField(max_length=10)
    stock = models.IntegerField()
    

class Transportista(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class OrdenDespacho(models.Model):
    fecha_creacion = models.DateField()
    fecha_despacho = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)

class DetalleOrden(models.Model):
    orden_despacho = models.ForeignKey(OrdenDespacho, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Supermercado(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Envio(models.Model):
    orden_despacho = models.ForeignKey(OrdenDespacho, on_delete=models.CASCADE)
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    fecha_envio = models.DateField()
    fecha_recepcion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)
