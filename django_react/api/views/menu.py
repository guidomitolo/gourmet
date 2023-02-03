from rest_framework import viewsets
from ..serializers.menu import MealSerializer, CategorySerializer
from menu.models import Meal, Category



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer