from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('cursos/', views.cursos, name='cursos'),
    path('inscripciones/', views.inscripciones, name='inscripciones'),
]