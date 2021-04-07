from django import forms
from django.shortcuts import render
from .forms import ConsultaForm


def comentarios(request):
    if request.method == "POST":
        form = ConsultaForm()
        if ConsultaForm.is_valid():
    form = ConsultaForm()
    context = {
        "form": form,
        "title": "comentarios"
    }
    return render(request, "comentarios/comentarios.html", context)
