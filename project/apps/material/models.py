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

    def __str__(self):
        return f"{self.ancho} {self.espesor}"


# Crear un Model más

# dato = input("Ingrese un número: ")
# numero = int(dato)
