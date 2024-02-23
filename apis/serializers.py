from rest_framework import serializers

from foodsMain.models import Food
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'title',
            'description',
            'price',
            'stars',
        )