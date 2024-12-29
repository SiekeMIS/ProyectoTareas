from django.db import models

class Tarea(models.Model):
    ESTADOS = [
        ('no_empezado', 'No empezado'),
        ('en_curso', 'En curso'),
        ('listo', 'Listo'),
    ]
    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES)
