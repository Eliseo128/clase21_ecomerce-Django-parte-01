from django.urls import path
from . import views

app_name = 'apptienda'

urlpatterns = [
    path('', views.todos_los_productos, name='todos_los_productos'),
    path('tienda/<slug:categoria_slug>/', views.lista_categoria, name='lista_categoria'), 
    path('<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    
]