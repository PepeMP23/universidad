from django.db import models

class Estudiante(models.Model):
    apellidos = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    fecha_inscripcion = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    creditos = models.IntegerField(null=True)

    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    id_curso = models.ForeignKey(
        Curso, null=True, blank=True, on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return Estudiante