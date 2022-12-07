from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.menu import ProductoViewSet
from .views.store import OrdenViewSet, OrdenarProductoViewSet, DespachoViewSet

router = DefaultRouter() 

router.register(r'producto', ProductoViewSet)
router.register(r'orden', OrdenViewSet)
router.register(r'ordenar_producto', OrdenarProductoViewSet)
router.register(r'despacho', DespachoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls))
]