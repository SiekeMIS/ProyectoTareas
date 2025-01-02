from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def listar_tareas(request):
    tareas = Tarea.objects.all().order_by('id')  # Ordena los datos por defecto
    paginator = Paginator(tareas, 5)  # 5 tareas por página

    page_number = request.GET.get('page')  # Obtiene el número de página actual
    page_obj = paginator.get_page(page_number)  # Obtiene los objetos de la página actual
    return render(request, 'ListarTareas.html', {'page_obj': page_obj})


def crear_tarea(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        estado = request.POST['estado']
        prioridad = request.POST['prioridad']
        Tarea.objects.create(nombre=nombre, descripcion=descripcion, estado=estado, prioridad=prioridad)
        return redirect('listar_tareas')
    return render(request, 'CrearTareas.html')

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.nombre = request.POST['nombre']
        tarea.descripcion = request.POST['descripcion']
        tarea.estado = request.POST['estado']
        tarea.prioridad = request.POST['prioridad']
        tarea.save()
        return redirect('listar_tareas')
    return render(request, 'ModificarTareas.html', {'tarea': tarea})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas')
    return render(request, 'EliminarTareas.html', {'tarea': tarea})
