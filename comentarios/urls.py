from django.urls import path
from . import views

urlpatterns = [
    # home view = sitio raíz
    path('', views.comentarios, name='comentarios'),
]