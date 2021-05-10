from django.shortcuts import redirect, render
from .forms import ConsultaForm
from .models import Consulta
from tienda.models import Orden
from django.contrib import messages
from tienda.helpers import carrito_cookie



def home(request):

    if request.user.is_authenticated:
        try:
            request.user.cliente
            cliente = request.user.cliente
            orden, creado = Orden.objects.get_or_create(cliente=cliente, completado=False)
            carrito_items = orden.total_orden_cantidad
        except:
            carrito_items = 20
    else:
        carrito_items = carrito_cookie(request)['carrito_items']

    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            mail = form.cleaned_data["mail"]
            descripcion = form.cleaned_data["descripcion"]

            subject = "Nueva consulta de " + nombre
            desde = mail
            destino = ["info@dominio.org"]
            mensaje_html = """<h1> Consulta de: """ + nombre + """</h1>"""+ \
                """</h2>""" + """<br/><h2>Mail :""" + mail + """</h2>"""+ \
                """<hr/><p>"""+ descripcion + """</p>"""
            send_mail(subject, mensaje, desde, destino, html_message=mensaje_html, fail_silently=False)

            subject2 = "Consulta enviada satisfactoriamente - EMPRESA"
            desde2 = "info@dominio.org"
            destino2 = [mail]
            mensaje_html2 = """<h1> Tu mensaje ha sido enviado exitosamente</h1>
                        <h2>En breve nos estaremos comunicando</<h2>
                        <p>Este es un mail automático que no debe ser respondido.</p>"""
            send_mail(subject2, mensaje, desde2, destino2, html_message=mensaje_html2, fail_silently=False)

            com = Consulta(nombre=nombre, mail=mail, descripcion=descripcion)
            com.save()
            params = {}
            params['form'] = form
            messages.success(request, f'¡Hemos recibido tu mensaje!')

            return redirect("home")
        else:
            messages.success(request, f'¡Campos incompletos!')

    form = ConsultaForm()

    context = {
        "form": form,
        "title": "Home",
        'carrito_items': carrito_items,
    }

    return render(request, 'main/home.html', context)

def about(request):

    context = {
        'title': 'About',
    }
    return render(request, 'main/about.html', context)