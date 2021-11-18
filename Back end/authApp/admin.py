from django.contrib import admin

from .models.proveedor import Proveedor
from .models.categoria import Categoria
from .models.producto import Producto


admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
# Register your models here.
