from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.menu import MealViewSet
from .views.store import OrderViewSet, OrderMealViewSet, DispachViewSet

router = DefaultRouter() 

router.register(r'meal', MealViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_meal', OrderMealViewSet)
router.register(r'dispach', DispachViewSet)


urlpatterns = [
    path('', include(router.urls)),
]