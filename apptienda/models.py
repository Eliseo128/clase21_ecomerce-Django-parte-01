from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductoManager(models.Manager):
    def get_queryset(self):
        return super(ProductoManager, self).get_queryset().filter(en_activo=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categorias'

    def get_absolute_url(self):
        return reverse('apptienda:lista_categoria', args=[self.slug])

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='producto', on_delete=models.CASCADE)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producto_creadopor')
    titulo= models.CharField(max_length=255)
    autor = models.CharField(max_length=255, default='admin')
    descrpcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='imagenes/productos', default='imaganes/productos/default.png')
    slug = models.SlugField(max_length=255)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    en_almacen = models.BooleanField(default=True)
    en_activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    objetos = models.Manager()
    productos = ProductoManager()

    class Meta:
        verbose_name_plural = 'Productos'
        ordering = ('-creado',)

    def get_absolute_url(self):
        return reverse('apptienda:detalle_producto', args=[self.slug])

    def __str__(self):
        return self.titulo