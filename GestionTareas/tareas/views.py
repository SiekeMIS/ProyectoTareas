from django.shortcuts import render

# Create your views here.
from tareas.models import Tarea

Tarea.objects.create(nombre="Tarea 1", descripcion="Descripción de la tarea 1", estado="no_empezado", prioridad="alta")
