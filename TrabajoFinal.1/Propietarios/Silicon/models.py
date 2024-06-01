from django.db import models

class Avance(models.Model):
    descripcion = models.TextField()
    progreso = models.IntegerField()
    fecha = models.DateField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_contacto = models.DateField()