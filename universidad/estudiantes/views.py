from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def estudiantes(request):
    template = loader.get_template('estudiantes.html')
    return HttpResponse(template.render())