from django.contrib import admin

from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'slug', 'precio', 'en_almacen', 'creado', 'actualizado']
    list_filter = ['en_almacen','en_activo']
    list_editable = ['precio', 'en_almacen']
    prepopulated_fields = {'slug': ('titulo',)}




