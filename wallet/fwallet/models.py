

from django.db import models
from django.contrib.auth.models import AbstractUser


#id, monto, tipo(ingreso, gasto, deuda), nombre(si es que es gasto, a quien le pagaste si es que es ingreso, quien te pago)
#fecha, clases de gasto, descripción

#Consultas sql para filtrar y metodos para ingresar datos a la base de datos

# Create your models here.

class User(AbstractUser):
    apodo = models.CharField(max_length=30)

small_size = 20
medium_size = 1000
class RegistroDinero(models.Model):

    monto = models.IntegerField()
    tipos_de_gasto = [('i','ingreso'), ('g','gasto'), ('d','deuda')]
    tipo = models.CharField(max_length=small_size, choices=tipos_de_gasto)
    nombre = models.CharField(max_length = small_size)
    fecha = models.DateField()
    clase = models.CharField(max_length=small_size)
    descripcion = models.CharField(max_length=medium_size)
