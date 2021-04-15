from django.shortcuts import render

# Create your views here.

def tienda(request):
    context = {"title":"Tienda"}
    return render(request, "tienda/tienda.html", context)

def carrito(request):
    context = {"title":"Carrito"}
    return render(request, "tienda/carrito.html", context)

def checkout(request):
    context = {"title":"Checkout"}
    return render(request, "tienda/checkout.html", context)
