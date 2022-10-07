from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Inventarios, Cliente, Sucursal, Producto

# Register your models here.

admin.site.register(Inventarios)
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Producto)


# Register your models here.
class InventarioInline(admin.StackedInline):
    model = Inventarios
    can_delete = False
    verbose_name_plural = 'Inventarios'
class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'Clientes'
class SucursalInline(admin.StackedInline):
    model = Sucursal
    can_delete = False
    verbose_name_plural = 'Sucursales'
class ProductoInline(admin.StackedInline):
    model = Producto
    can_delete = False
    verbose_name_plural = 'Productos'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

title = "Inventario"
subtitle = "Gestión DB inventario"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle