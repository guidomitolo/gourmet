from rest_framework import serializers
from store.models import Order, OrderMeal, Dispach



class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"


class OrderMealSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderMeal
        fields = "__all__"


class DispachSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dispach
        fields = "__all__"