from inspect import formatannotation
from pyclbr import Class

from django.db import models

# Create your models here.


class Material(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Dimension(models.Model):
    largo = models.IntegerField(max_length=20)
    ancho = models.IntegerField(max_length=20)
    espesor = models.IntegerField(max_length=20)
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.largo} {self.ancho} {self.espesor}"


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f" {self.nombre} {self.pais}"
