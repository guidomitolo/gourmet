from django.contrib import admin
from .models import User, Cliente, Empleado, Profile

class UserAdmin(admin.ModelAdmin):

    # campo de orden por fecha segun ultima modificación
    date_hierarchy = 'last_login'
    # campo de busqueda por nombre
    search_fields = ['first_name']
    # campos a mostrar en total de registros
    list_display = ['username','date_joined','last_login','is_active','is_customer','is_employee','is_staff','is_superuser']
    # ordenar segun modificacion y publicacion
    ordering = ['-username']
    # filtros
    list_filter = ('is_customer','is_employee','is_superuser')

    list_per_page = 25

admin.site.register(Profile)
admin.site.register(User, UserAdmin)
admin.site.register(Cliente)
admin.site.register(Empleado)