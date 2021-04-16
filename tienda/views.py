from django.shortcuts import render
from menu.models import Producto
from menu.forms import BuscarProducto
from .models import Orden, OrdenarProducto, Despacho

from django.http import JsonResponse

import json


import datetime



def tienda(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad
    else:
        orden = {"total_orden_precio": 0, "total_orden_cantidad": 0}
        items = []
        carrito_items = orden["total_orden_cantidad"]

    # if request.method == 'POST':
    #     if request.POST.get('eliminar'):
    #         Producto.objects.filter(id = request.POST['eliminar']).delete()
    #         return redirect("menu")
    #     elif request.POST.get('buscar'):
    #         productos = Producto.objects.filter(nombre=request.POST.get("productos"))
    # else:
    #     productos = Producto.objects.filter(estado='Publicado')

    productos = Producto.objects.filter(estado='Publicado')

    return render(request, 'tienda/tienda.html', {
        'title': 'Tienda',
        'items': productos,
        'buscar': BuscarProducto(),
        'carrito_items':carrito_items
        }
    )

def carrito(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad
    else:
        orden = {"total_orden_precio": 0, "total_orden_cantidad": 0}
        items = []
        carrito_items = orden["total_orden_cantidad"]

    context = {
        "title":"Carrito",
        "items": items,
        "orden": orden,
        'carrito_items':carrito_items
        }

    return render(request, "tienda/carrito.html", context)

def checkout(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad
    else:
        orden = {"total_orden_precio": 0, "total_orden_cantidad": 0}
        items = []
        carrito_items = orden["total_orden_cantidad"]

    context = {
        "title":"Checkout",
        "items": items,
        "orden": orden,
        'carrito_items':carrito_items
        }
    
    return render(request, "tienda/checkout.html", context)


def actualizar_producto(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    cliente = request.user.cliente
    producto = Producto.objects.get(id=productId)
    orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)

    ordenarItem, creado = OrdenarProducto.objects.get_or_create(orden=orden, producto=producto)

    if action == 'add':
        ordenarItem.cantidad = (ordenarItem.cantidad + 1)
    elif action == 'remove':
        ordenarItem.cantidad = (ordenarItem.cantidad - 1)

    ordenarItem.save()

    if ordenarItem.cantidad <= 0:
        ordenarItem.delete()

    return JsonResponse("El producto fue agregado", safe=False)


def procesar_orden(request):
    data = json.loads(request.body)
    trans_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        total = float(data['form']['total'])
        orden.trans_id = trans_id

        if total == orden.total_orden_precio:
            orden.completado = True
        orden.save()

        Despacho.objects.create(
            cliente = cliente,
            orden = orden,
            direccion = data['despacho']['address'],
            ciudad = data['despacho']['city'],
            estado = data['despacho']['state'],
            postal = data['despacho']['zipcode'],
        )

    else:
        print("user is not logged in")

    return JsonResponse("Payment complete", safe=False)
