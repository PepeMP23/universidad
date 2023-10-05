from django.contrib import admin
from .models import Estudiante, Curso, Inscripcion

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
  list_display = ("nombres", "apellidos", "fecha_inscripcion",)
  
admin.site.register(Estudiante, EstudianteAdmin)

class CursoAdmin(admin.ModelAdmin):
  list_display = ("titulo", "creditos",)
  
admin.site.register(Curso, CursoAdmin)

class InscripcionAdmin(admin.ModelAdmin):
  list_display = ("id_curso", "id_estudiante",)
  
admin.site.register(Inscripcion, InscripcionAdmin)