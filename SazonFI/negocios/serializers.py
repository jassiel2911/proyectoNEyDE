from rest_framework import serializers
from .models import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = '__all__'  # O fields = ['id', 'nombre', 'descripcion', 'direccion', 'usuario']
        read_only_fields = ['usuario']
