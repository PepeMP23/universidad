from django.db import models

class hola(models.Model):
    titulo = models.CharField(max_length=255)
    creditos = models.IntegerField(null=True)