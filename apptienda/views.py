from django.shortcuts import render,get_object_or_404
from .models import Categoria, Producto

def todos_los_productos(request):
    productos = Producto.productos.all()
    return render(request, 'apptienda/home.html', {'productos': productos})

def lista_categoria(request, categoria_slug=None):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.productos.filter(categoria=categoria)
    return render(request, 'apptienda/productos/categoria.html', {'categoria': categoria, 'productos': productos})

def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, en_almacen=True)
    return render(request, 'apptienda/productos/producto.html', {'producto': producto})
    



# Create your views here.
