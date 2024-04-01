from django.contrib import admin
from django.urls import path
from calculator.views import index, calculate_consumption

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),  # Adiciona esta rota para a view 'index'
    path('form/', calculate_consumption, name='form'),  # Altera a rota para apontar para a view 'calculate_consumption'
]
