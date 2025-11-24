from django.test import TestCase
from restaurant import services
from restaurant.models import Restaurant, MenuItem


class ServicesTest(TestCase):
    def test_create_restaurant_with_default_menu(self):
        resto = services.create_restaurant_with_default_menu("Service Resto")
        self.assertIsInstance(resto, Restaurant)
        self.assertTrue(MenuItem.objects.filter(restaurant=resto).exists())
