from inspect import formatannotation
from pyclbr import Class

from django.db import models

# Create your models here.


class Material(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Dimensiones(models.Model):
    largo = models.CharField(max_length=20)
    ancho = models.CharField(max_length=20)
    espesor = models.CharField(max_length=20)
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.largo} {self.ancho} {self.espesor} {self.material_id}"


class Pais_Origen(models.Model):
    nombre = models.CharField(max_length=50)
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
