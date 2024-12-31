from django.shortcuts import render
from django.shortcuts import render
from .models import Tarea

def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'vistatareas.html', {'tareas': tareas})
