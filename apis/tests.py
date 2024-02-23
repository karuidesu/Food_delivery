from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from foodsMain.models import Food

# Create your tests here.
    
class FoodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.food = Food.objects.create(
            title = 'Red Velvet Cake',
            description = 'Moist red velvet cake with cream cheese frosting.',
            price = 29.99,
            stars = 4
        )
        
    def test_model_content(self):
        self.assertEqual(self.food.title, 'Red Velvet Cake')   
        self.assertEqual(self.food.description, 'Moist red velvet cake with cream cheese frosting.')
        self.assertEqual(self.food.price, 29.99)
        self.assertEqual(self.food.stars, 4)
        
    def test_api_listview(self):
        response = self.client.get(reverse('food_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Food.objects.count(), 1)
        self.assertContains(response, self.food)
        
    def test_api_detailview(self):
        response = self.client.get(
            reverse('food_detail', kwargs={'pk': self.food.pk}),
            format = 'json'
        )    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Food.objects.count(), 1)
        self.assertContains(response, 'Red Velvet Cake')
        
        
        
"""
#first test
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
    """