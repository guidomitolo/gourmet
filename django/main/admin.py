from django.contrib import admin
from main.models import Consulta, Respuesta

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0

class Consultaadmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ['nombre', 'descripcion', 'mail', 'estado_respuesta', 'fecha']
    list_filter = ('estado_respuesta','fecha')

admin.site.register(Consulta, Consultaadmin)

