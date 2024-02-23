from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    stars = models.CharField(max_length=13)
    author = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    