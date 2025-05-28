from django.contrib import admin
from .models import Electrodomestico

@admin.register(Electrodomestico)
class ElectrodomesticoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio', 'fecha_publicacion')
    search_fields = ('nombre', 'marca')
    list_filter = ('marca', 'precio')