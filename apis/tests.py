from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from foodsMain.models import Food

# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.food = Food.objects.create(
            title = 'Red Velvet Cake',
            description = 'Moist red velvet cake with cream cheese frosting.',
            price = 29.99,
            stars = 4
            )
        
    def test_api_listview(self):
        response = self.client.get(reverse("food_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Food.objects.count(), 1)
        self.assertContains(response, self.food)
        
        