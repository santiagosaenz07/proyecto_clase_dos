from django.urls import path
from .views import ListaCrearElectrodomestico, DetalleElectrodomestico, ListaCrearComentario

urlpatterns = [
    path('productos/', ListaCrearElectrodomestico.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', DetalleElectrodomestico.as_view(), name='detalle_electrodomestico'),
    path('comentarios/', ListaCrearComentario.as_view(), name='lista_comentarios'),
]
