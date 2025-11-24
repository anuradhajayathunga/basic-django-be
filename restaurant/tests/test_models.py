from django.test import TestCase
from restaurant.models import Restaurant, MenuItem


class RestaurantModelTest(TestCase):
    def test_str_returns_name(self):
        resto = Restaurant.objects.create(name="Test Resto")
        self.assertEqual(str(resto), "Test Resto")
