from django.urls import path
from . import views

urlpatterns = [
    path('inscripciones/', views.inscripciones, name='inscripciones'),
]