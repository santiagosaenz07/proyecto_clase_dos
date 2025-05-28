import django_filters
from .models import Electrodomestico

class ElectrodomesticoFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(field_name="precio", lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name="precio", lookup_expr='lte')

    class Meta:
        model = Electrodomestico
        fields = ['marca', 'vendedor', 'tipo', 'precio_min', 'precio_max']