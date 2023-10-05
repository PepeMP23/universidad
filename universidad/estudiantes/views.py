from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Estudiante, Curso, Inscripcion

def testing(request):
    template = loader.get_template('testing.html')
    return HttpResponse(template.render())

def estudiantes(request):
  mydata = Estudiante.objects.all()
  template = loader.get_template('estudiantes.html')
  context = {
    'misestudiantes': mydata,
  }
  return HttpResponse(template.render(context, request))

def cursos(request):
  mydata = Curso.objects.all()
  template = loader.get_template('cursos.html')
  context = {
    'miscursos': mydata,
  }
  return HttpResponse(template.render(context, request))

def inscripciones(request):
  mydata = Inscripcion.objects.all()
  template = loader.get_template('inscripciones.html')
  context = {
    'misinscripciones': mydata,
  }
  return HttpResponse(template.render(context, request))
