from rest_framework import serializers
from menu.models import Meal



class MealSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meal
        fields = "__all__"