from rest_framework import generics
from .models import Electrodomestico, Comentario
from .serializers import ElectrodomesticoSerializer, ComentarioSerializer
from .filters import ElectrodomesticoFilter  
from .pagination import ElectrodomesticoPagination

class ListaCrearElectrodomestico(generics.ListCreateAPIView):
    queryset = Electrodomestico.objects.all()
    serializer_class = ElectrodomesticoSerializer
    filterset_class = ElectrodomesticoFilter  # <-- Usa tu filtro personalizado
    pagination_class = ElectrodomesticoPagination  # <-- Agrega esta línea


class DetalleElectrodomestico(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electrodomestico.objects.all()
    serializer_class = ElectrodomesticoSerializer

class ListaCrearComentario(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
