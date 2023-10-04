from django.db import models

class Estudiante(models.Model):
    apellidos = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    fecha_inscripcion = models.DateField(null=True)