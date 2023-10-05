from django.db import models

class Estudiante(models.Model):
    apellidos = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    fecha_inscripcion = models.DateField(null=True)

    def _str_(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    creditos = models.IntegerField(null=True)

    def _str_(self):
        return self.titulo

class Inscripcion(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id_curso} {self.id_estudiante}"