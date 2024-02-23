from django.urls import path
from .views import FoodAPIView, DetailFood, ListFood

urlpatterns = [

    path('<int:pk>/', DetailFood.as_view(), name='food_detail'),
    path('', ListFood.as_view(), name='food_list')
]
