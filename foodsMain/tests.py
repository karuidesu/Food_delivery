from django.test import TestCase
from django.urls import reverse
from .models import Food
from django.contrib.auth import get_user_model

# Create your tests here.

class FoodTests(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@example.com',
            password = 'secret',
        )
        
        cls.food = Food.objects.create(
            title = 'Chocolate Cake',
            description = "Delicious chocolate cake with rich flavor.",
            price = 25.99,
            stars = 4,
            author = cls.user,
        )

    
    def test_food_content(self):
        self.assertEqual(self.food.title, "Chocolate Cake")
        self.assertEqual(self.food.description, "Delicious chocolate cake with rich flavor.")
        self.assertEqual(self.food.price, 25.99)
        self.assertEqual(self.food.stars, 4)
        self.assertEqual(self.food.author.username, 'testuser')
        
    def test_food_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "chocolate cake")
        self.assertTemplateUsed(response, "food/index.html")