from django.contrib import admin
from django.urls import path
from calculator.views import index, calcularConsumo, listar_consumidores_economia

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'), 
    path('form/', calcularConsumo, name='form'),  
    path('listar_consumidores_economia/', listar_consumidores_economia, name='listar_consumidores_economia')
]

