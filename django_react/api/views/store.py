from rest_framework import viewsets
from ..serializers.store import OrderSerializer, OrderMealSerializer, DispachSerializer
from store.models import Order, OrderMeal, Dispach



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderMealViewSet(viewsets.ModelViewSet):
    queryset = OrderMeal.objects.all()
    serializer_class = OrderMealSerializer


class DispachViewSet(viewsets.ModelViewSet):
    queryset = Dispach.objects.all()
    serializer_class = DispachSerializer