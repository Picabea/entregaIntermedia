from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


class Aula(models.Model):
    materia = models.CharField(max_length=40)
    numero = models.IntegerField()
    tamaño = models.IntegerField()


class Edificio(models.Model):
    pisos = models.IntegerField()
    facultad = models.CharField(max_length=40)
    cantidad_de_aulas = models.IntegerField()