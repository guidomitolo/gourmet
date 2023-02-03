from rest_framework import serializers
from store.models import Order, OrderMeal, Dispach
from users.models import Customer
from .menu import MealSerializer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    
    class Meta:
        model = Order
        fields = "__all__"


class OrderMealSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    meal = MealSerializer()
    
    class Meta:
        model = OrderMeal
        fields = "__all__"


class DispachSerializer(serializers.ModelSerializer):
    
    order = OrderSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Dispach
        fields = "__all__"