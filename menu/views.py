from users.decorators import allowed_users
from django.shortcuts import render, redirect

from menu.models import Producto, Categoria
from menu.forms import CargarProducto, AgregarCategoria, EliminarCategoria, BuscarProducto

from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

# busqueda con AJAX
from django.views.generic import View
import json
from django.http import HttpResponse


def menu(request):


    if request.method == 'POST':
        if request.POST.get('eliminar'):
            Producto.objects.filter(id = request.POST['eliminar']).delete()
            return redirect("menu")
        elif request.POST.get('buscar'):
            productos = Producto.objects.filter(nombre=request.POST.get("productos"))
    else:
        productos = Producto.objects.filter(estado='Publicado')
    
    return render(request, 'menu/menu.html', {
        'title': 'Menu',
        'items': productos,
        'buscar': BuscarProducto()
        }
    )


class BuscarProducto(View):

    def get(self, request):
        if request.is_ajax:
            palabra = request.GET.get('term', '')
            libro = Producto.objects.filter(nombre__icontains=palabra)
            results = []
            for an in libro:
                data = {}
                data['label'] = an.nombre
                results.append(data)
            data_json = json.dumps(results)
        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)


@login_required
@allowed_users(allowed_roles=['empresa'])
def modificar(request, item_id):

    if request.method == 'POST':
        pr_form = CargarProducto(request.POST, request.FILES, instance=Producto.objects.filter(id=item_id).first())
        update_doc = Producto.objects.filter(id=item_id).first()

        if pr_form.is_valid():
            update_doc.nombre = pr_form.cleaned_data['nombre']
            update_doc.detalle = pr_form.cleaned_data['detalle']
            update_doc.ruta_imagen = pr_form.cleaned_data['ruta_imagen']
            update_doc.vegano = pr_form.cleaned_data['vegano']
            update_doc.delivery = pr_form.cleaned_data['delivery']
            update_doc.celiaco = pr_form.cleaned_data['celiaco']
            update_doc.precio = pr_form.cleaned_data['precio']
            update_doc.estado = pr_form.cleaned_data['estado']
            update_doc.save()
            
            # agregar categorias elegidas
            for categoria in pr_form.cleaned_data['categoria']:
                if categoria not in update_doc.categoria.all():
                    update_doc.categoria.add(categoria)
            # eliminar las no elegidas
            for categoria in update_doc.categoria.all():
                if categoria not in pr_form.cleaned_data['categoria']:
                    update_doc.categoria.remove(categoria)

            return redirect("menu")

    else:
        pr_form = CargarProducto(instance=Producto.objects.filter(id=item_id).first())
    
    return render(request, 'menu/modificar.html', {'pr_form': pr_form})


@login_required
@allowed_users(allowed_roles=['empresa'])
def cargar_carta(request):

    if request.method == 'POST':
        pr_form = CargarProducto(request.POST, request.FILES)
        add_cat = AgregarCategoria(request.POST)
        del_cat = EliminarCategoria(request.POST)

        if request.POST.get('agregar'):

            if add_cat.is_valid():

                nombre = add_cat.cleaned_data['nombre']
                slug = add_cat.cleaned_data['slug']

                cat = Categoria(
                    nombre=nombre, 
                    slug=slug
                    )
                cat.save()

                return redirect("cargar")

        elif request.POST.get('eliminar'):

            if del_cat.is_valid():

                for cat_to_del in del_cat.cleaned_data['categoria']:
                    Categoria.objects.filter(id=cat_to_del.id).delete()

                return redirect("cargar")

        elif request.POST.get('cargar'):

            if pr_form.is_valid():
                newdoc = Producto(
                    nombre = pr_form.cleaned_data['nombre'],
                    detalle = pr_form.cleaned_data['detalle'],
                    ruta_imagen = pr_form.cleaned_data['ruta_imagen'],
                    vegano = pr_form.cleaned_data['vegano'],
                    delivery = pr_form.cleaned_data['delivery'],
                    celiaco = pr_form.cleaned_data['celiaco'],
                    precio = pr_form.cleaned_data['precio'],
                    usuario = request.user,
                    estado = pr_form.cleaned_data['estado']
                )
                newdoc.save()

                for cat in pr_form.cleaned_data['categoria']:
                    newdoc.categoria.add(cat)

                return redirect("menu")
    else:
        pr_form = CargarProducto()
        add_cat = AgregarCategoria()
        del_cat = EliminarCategoria()
    
    return render(request, 'menu/cargar.html', {'pr_form': pr_form, 'del_cat': del_cat ,'add_cat': add_cat})

def promos(request):
    context = {
        "title": "Promos"
    }
    return render(request, "main/promos.html", context)
