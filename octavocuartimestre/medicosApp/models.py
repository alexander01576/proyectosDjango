from django.utils import timezone
from django.db import models

# Create your models here.

class inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombreMat = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombreMat


class medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nomMed = models.CharField(max_length=100)
    aPat = models.CharField(max_length=100)
    aMat = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)

    def __str__(self):
        return self.nomMed


class conferencia(models.Model):
    id_conferencia = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return self.tema


class consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    fechaConsulta = models.DateField(default=timezone.now)
    nombrePaci = models.CharField(max_length=100)
    apPatPaci = models.CharField(max_length=100)
    apMatPaci = models.CharField(max_length=100)
    edadPaci = models.IntegerField()
    sexoPaci = models.CharField(max_length=100)
    tipoPaci = models.CharField(max_length=100)
    motivoCons = models.CharField(max_length=500)
    solucion = models.CharField(max_length=500)
 
    def __str__(self):
        return self.motivoCons
