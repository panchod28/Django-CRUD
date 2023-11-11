from django.db import models

# Create your models here.

class Vehiculos(models.Model):
    VehiculoId = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=50, null=True, blank=True)
    ano = models.CharField(max_length=4, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    valorDia = models.CharField(max_length=10, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    imagen = models.TextField(null=True, blank=True)
