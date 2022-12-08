from rest_framework import viewsets
from ..serializers.menu import MealSerializer
from menu.models import Meal



class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
