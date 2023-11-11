from rest_framework import serializers
from Vehiculos.models import Vehiculos

class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = ('VehiculoId', 'identificador', 'tipo', 'modelo', 'marca', 'ano', 'descripcion', 'valorDia', 'estado', 'imagen')