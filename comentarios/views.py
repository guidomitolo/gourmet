from django.shortcuts import redirect, render
from .forms import ConsultaForm
from .models import Consulta


def comentarios(request):
    if request.method == "POST":
        form = ConsultaForm()
        if ConsultaForm.is_valid():
            nombre = form.cleaned_data["nombre"]
            mail = form.cleaned_data["mail"]
            descripcion = form.cleaned_data["descripcion"]

            # ############MESAJE DIRIGIDO AL SITIO #####################
            subject = "Nueva consulta de " + nombre
            desde = mail
            destino = ["info@dominio.org"]
            mensaje_html = """<h1> Consulta de: """ + nombre + """</h1>"""+ \
                """</h2>""" + """<br/><h2>Mail :""" + mail + """</h2>"""+ \
                """<hr/><p>"""+ descripcion + """</p>"""
            #send_mail(subject, mensaje, desde, destino, html_message=mensaje_html, fail_silently=False)

            # ############MESAJE DIRIGIDO AL USUARIO #####################

            subject2 = "Consulta enviada satisfactoriamente - EMPRESA"
            desde2 = "info@dominio.org"
            destino2 = [mail]
            mensaje_html2 = """<h1> Tu mensaje ha sido enviado exitosamente</h1>
                        <h2>En breve nos estaremos comunicando</<h2>
                        <p>Este es un mail automático que no debe ser respondido.</p>"""
            #send_mail(subject2, mensaje, desde2, destino2, html_message=mensaje_html2, fail_silently=False)

            com = Consulta(nombre=nombre, mail=mail, descripcion=descripcion)
            com.save()
            params = {}
            params['form'] = form

            return redirect("home")

    form = ConsultaForm()
    context = {
        "form": form,
        "title": "comentarios"
    }
    return render(request, "comentarios/comentarios.html", context)
