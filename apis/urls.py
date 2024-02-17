from django.urls import path
from .views import FoodAPIView

urlpatterns = [
    path('', FoodAPIView.as_view(), name='food_list')
]
