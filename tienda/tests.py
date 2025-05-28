from django.test import TestCase
from .models import Electrodomestico

class ElectrodomesticoModelTest(TestCase):
    def setUp(self):
        Electrodomestico.objects.create(nombre="Lavadora", precio=150.00, descripcion="Lavadora usada en buen estado")
        Electrodomestico.objects.create(nombre="Refrigerador", precio=300.00, descripcion="Refrigerador usado, funciona perfectamente")

    def test_electrodomestico_creation(self):
        lavadora = Electrodomestico.objects.get(nombre="Lavadora")
        refrigerador = Electrodomestico.objects.get(nombre="Refrigerador")
        self.assertEqual(lavadora.precio, 150.00)
        self.assertEqual(refrigerador.descripcion, "Refrigerador usado, funciona perfectamente")