from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Restaurant


class RestaurantAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
        )

        # Get JWT token
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url,
            {"username": "testuser", "password": "password123"},
            format="json",
        )
        self.access = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")

    def test_create_restaurant(self):
        url = reverse("restaurant-list")
        data = {"name": "API Resto"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
