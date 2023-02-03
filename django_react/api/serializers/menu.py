from rest_framework import serializers
from menu.models import Meal, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MealSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True)
    
    class Meta:
        model = Meal
        fields = "__all__"