from django.shortcuts import redirect, render
from menu.models import Producto, Categoria
from menu.forms import BuscarProducto

from .models import Orden, OrdenarProducto, Despacho

from users.models import Cliente
from django.contrib.auth import get_user_model
User = get_user_model()

from django.http import JsonResponse
import json

from .helpers import carrito_cookie, carrito_info
import datetime


def tienda(request):

    if request.user.is_authenticated:
        # el usuario logueado es cliente
        try:
            request.user.cliente
            cliente = request.user.cliente
            orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
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
        except:
            # el usuario logueado no es cliente -> sólo mostrar
            categorias = Categoria.objects.all()
            productos = None

            if request.method == 'POST':
                if request.POST.get('buscar'):
                    productos = Producto.objects.filter(nombre=request.POST.get("productos"))

            return render(request, 'tienda/tienda.html', {
                'title': 'Tienda',
                'items': productos,
                'buscar': BuscarProducto(),
                'categorias':categorias
                }
            )
    else:
        # usuario fantasma/invitado
        categorias = Categoria.objects.all()
        productos = None

        if request.method == 'POST':
            if request.POST.get('buscar'):
                productos = Producto.objects.filter(nombre=request.POST.get("productos"))

        return render(request, 'tienda/tienda.html', {
            'title': 'Tienda',
            'items': productos,
            'buscar': BuscarProducto(),
            'carrito_items':carrito_cookie(request)['carrito_items'],
            'categorias':categorias
            }
        )

def carrito(request):

    return render(request, "tienda/carrito.html", carrito_info(request))


def checkout(request):
    
    return render(request, "tienda/checkout.html", carrito_info(request))


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
        # si el usuario y cliente está logueado, actualizar base de datos con el formulario        
        cliente_db = Cliente.objects.get(user = request.user)
        cliente_db.calle = data['despacho']['calle']
        cliente_db.altura = data['despacho']['altura']
        cliente_db.municipio = data['despacho']['municipio']
        cliente_db.localidad = data['despacho']['localidad']
        cliente_db.save()
        
        usuario = User(id = request.user.id)
        usuario.nombre = data['form']['nombre']
        usuario.apellido = data['form']['apellido']
        usuario.email = data['form']['email']
        usuario.save()
    
    else:
        # si el usuario no está registrado, crear orden y usuario
        nombre = data['form']['nombre']
        apellido = data['form']['apellido']
        email = data['form']['email']

        cookie_data = carrito_info(request)
        items = cookie_data['items']

        # creo una entrada en la DB con el ususario fantasma
        fantasma, creado = User.objects.get_or_create(
            email = email
        )
        fantasma.is_customer = True
        fantasma.is_guest = True
        fantasma.first_name = nombre
        fantasma.last_name = apellido
        fantasma.save()

        cliente, creado = Cliente.objects.get_or_create(
            user = fantasma
        )

        orden = Orden.objects.create(
            cliente = cliente,
            completado = False
        )

        for item in items:

            producto = Producto.objects.get(id=item['producto']['id'])

            item_orden = OrdenarProducto.objects.create(
                producto = producto,
                orden = orden,
                cantidad = item['cantidad']                
            )

    Despacho.objects.create(
        cliente = cliente,
        orden = orden,
        calle = data['despacho']['calle'],
        altura = data['despacho']['altura'],
        municipio = data['despacho']['municipio'],
        localidad = data['despacho']['localidad'],
    )

    total = float(data['form']['total'])
    orden.trans_id = trans_id

    if total == orden.total_orden_precio:
        orden.completado = True
        
    orden.save()


    return JsonResponse("Payment complete", safe=False)
