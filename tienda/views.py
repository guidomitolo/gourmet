from django.shortcuts import redirect, render
from menu.models import Producto, Categoria
from menu.forms import BuscarProducto
from .models import Orden, OrdenarProducto, Despacho

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json

import datetime


@login_required
def tienda(request):

    if request.user.is_customer:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad
        
        categorias = Categoria.objects.all()
        productos = None

        if request.method == 'POST':
            if request.POST.get('buscar'):
                productos = Producto.objects.filter(nombre=request.POST.get("productos"))

        return render(request, 'tienda/tienda.html', {
            'title': 'Tienda',
            'items': productos,
            'buscar': BuscarProducto(),
            'carrito_items':carrito_items,
            'categorias':categorias
            }
        )
    else:
        messages.success(request, f'Usted no es cliente')
        return redirect("menu")

@login_required
def carrito(request):

    if request.user.is_customer:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad

        context = {
            "title":"Carrito",
            "items": items,
            "orden": orden,
            'carrito_items':carrito_items
            }

        return render(request, "tienda/carrito.html", context)
    else:
        messages.success(request, f'Usted no es cliente')
        return redirect("menu")

@login_required
def checkout(request):

    if request.user.is_customer:
        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad

        context = {
            "title":"Checkout",
            "items": items,
            "orden": orden,
            'carrito_items':carrito_items
            }
    
        return render(request, "tienda/checkout.html", context)
    else:
        messages.success(request, f'Usted no es cliente')
        return redirect("menu")

@login_required
def actualizar_producto(request):

    if request.user.is_customer:

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
    else:
        messages.success(request, f'Usted no es cliente')
        return redirect("menu")

@login_required
def procesar_orden(request):

    if request.user.is_customer:
        data = json.loads(request.body)
        trans_id = datetime.datetime.now().timestamp()
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
            calle = data['despacho']['calle'],
            altura = data['despacho']['altura'],
            municipio = data['despacho']['municipio'],
            localidad = data['despacho']['localidad'],
        )

        return JsonResponse("Payment complete", safe=False)
    else:
        messages.success(request, f'Usted no es cliente')
        return redirect("menu")
