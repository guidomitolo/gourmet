import json
from menu.models import Producto
from tienda.models import Orden

from users.forms import ActualizarCliente, ActualizarUsuario


def carrito_cookie(request):

    try:
        carrito = json.loads(request.COOKIES['cart'])
    except:
        carrito = {}

    # creo un diccionario con la orden para luego crear la cookie
    orden = {'total_orden_precio': 0, 'total_items': 0}
    items = []
    carrito_items = orden['total_items']

    try:
        for item_id in carrito:

            producto = Producto.objects.get(id = item_id)
            carrito_items += carrito[item_id]['quantity']
            total = producto.precio * carrito[item_id]['quantity']

            orden['total_orden_precio'] += total
            orden['total_items'] += carrito[item_id]['quantity']

            item = {
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'ruta_imagen': producto.ruta_imagen,
                },
                'cantidad': carrito[item_id]['quantity'],
                'total_precio': total
            }

            items.append(item)

        context = {
            "title":"Carrito",
            "items": items,
            "orden": orden,
            'carrito_items':carrito_items
        }
    except:
        print("CARRITO ITEMS", carrito_items)
        context = {
            "title":"Carrito",
            "items": items,
            "orden": orden,
            'carrito_items':carrito_items
        }
                
    return context


def carrito_info(request):

    if request.user.is_authenticated:

        cliente = request.user.cliente
        orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenarproducto_set.all()
        carrito_items = orden.total_orden_cantidad

        form_destino = ActualizarCliente(instance=request.user.cliente)
        form_usuario = ActualizarUsuario(instance=request.user)

        context = {
            "title":"Carrito",
            "items": items,
            "orden": orden,
            'carrito_items': carrito_items,
            'form_usuario': form_usuario,
            'form_destino': form_destino
            }
    else:
        context = carrito_cookie(request)

    return context