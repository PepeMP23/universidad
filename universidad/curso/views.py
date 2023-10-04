from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def cursos(request):
  template = loader.get_template('cursos.html')
  return HttpResponse(template.render())