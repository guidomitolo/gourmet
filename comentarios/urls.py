from django.urls import path
from . import views

urlpatterns = [
    path('', views.comentarios, name='comentarios'),
]