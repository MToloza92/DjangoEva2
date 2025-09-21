from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'nombre', 'categoria', 'proveedor', 'precio', 'stock_actual')
    search_fields = ('nombre', 'sku')
    list_filter = ('categoria', 'proveedor')
