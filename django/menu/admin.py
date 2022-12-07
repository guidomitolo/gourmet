from django.contrib import admin
# importo los modelos creados
from menu.models import Producto, Categoria

# agrego acciones al sitio del administrador
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/
def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

def retirar(modeladmin, request, queryset):
    queryset.update(estado='Sin stock')

def pausar(modeladmin, request, queryset):
    queryset.update(estado='Pausado')


class CategoriaAdmin(admin.ModelAdmin):
    # autocompletar el slug con el nombre
    prepopulated_fields = {"slug": ("nombre",)}

class ProductoAdmin(admin.ModelAdmin):

    # campo de orden por fecha segun ultima modificación
    date_hierarchy = 'last_modified'
    # campo de busqueda por nombre
    search_fields = ['nombre']
    # campos a completar (usuario y fechas se completan automaticamente)
    fields =['categoria', 'nombre', 'detalle', 'celiaco', 'vegano', 'delivery', 'ruta_imagen', 'precio']
    # campos a mostrar en total de registros
    list_display = ['pub_date', 'last_modified','usuario', 'nombre', 'celiaco', 'vegano', 'delivery', 'precio','estado']
    # ordenar segun modificacion y publicacion
    ordering = ['-last_modified','-pub_date']
    # filtros
    list_filter = ('categoria', 'last_modified', 'celiaco', 'vegano', 'delivery')

    list_per_page = 25

    actions = [publicar, retirar, pausar]

    # autocompletar el usuario con el usuario logueado
    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)


# registro los modelos en el sitio del administador
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
