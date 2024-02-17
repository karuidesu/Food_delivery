from django.shortcuts import render
from rest_framework import generics
from foodsMain.models import Food
from .serializers import FoodSerializer

# Create your views here.


class FoodAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    template_name = 'food/index.html'
