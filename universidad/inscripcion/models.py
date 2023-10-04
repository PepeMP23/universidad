from django.db import models

class Inscripcion(models.Model):
    id_curso = models.IntegerField(null=True)
    id_estudiante = models.IntegerField(null=True)
