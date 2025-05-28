from rest_framework import serializers
from .models import Electrodomestico, Comentario

class ElectrodomesticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electrodomestico
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
