
from django.db import models
from django.contrib.auth.models import AbstractUser


#id, monto, tipo(ingreso, gasto, deuda), nombre(si es que es gasto, a quien le pagaste si es que es ingreso, quien te pago)
#fecha, clases de gasto, descripción

#Consultas sql para filtrar y metodos para ingresar datos a la base de datos

# Create your models here.

class User(AbstractUser):
    generos = [("m", "Masculino"), ("f", "Femenino"), ("nb", "No-binario"), ("Otro", "Otro")]
    genero = models.CharField(max_length = 13, choices = generos)
    apodo = models.CharField(max_length=30)

small_size = 20
medium_size = 1000


class RegistroDinero(models.Model):
    owner = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    monto = models.IntegerField()
    tipos_de_gasto = [('Ingreso','Ingreso'), ('Gasto','Gasto'), ('Deuda','Deuda')]
    tipo = models.CharField(max_length=small_size, choices=tipos_de_gasto)
    nombre = models.CharField(max_length = small_size)
    fecha = models.DateField()
    clase = models.CharField(max_length=small_size)
    descripcion = models.CharField(max_length=medium_size)
