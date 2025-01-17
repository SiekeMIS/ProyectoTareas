from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'descripcion', 'estado', 'prioridad')
        read_only_field = ('id',)