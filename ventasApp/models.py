from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    telefono = models.IntegerField()
    email = models.CharField(max_length=150)

class Colaborador(models.Model):
    cargo = models.CharField(max_length=100)
    jefe_directo = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)
    id_persona = models.IntegerField()
    contrasena = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    unidad_venta = models.CharField(max_length=100)
    precio = models.IntegerField()
    posicion = models.CharField(max_length=100)
    codigo_producto = models.IntegerField()

class Boleta(models.Model):
    numero_boleta = models.IntegerField()

class DetalleBoleta(models.Model):
    precio_total = models.IntegerField()
    iva = models.IntegerField()
    id_producto = models.IntegerField()
    metodo_pago = models.CharField(max_length=100)
    id_boleta = models.IntegerField()

class Venta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    codigo_producto = models.IntegerField()
    metodo_pago = models.CharField(max_length=100)
    iva = models.IntegerField()
    precio_total = models.IntegerField()
    numero_boleta = models.IntegerField()
    id_producto = models.IntegerField()