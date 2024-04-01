from django.contrib import admin
from django.urls import path
from calculator.views import index, calcularConsumo

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'), 
    path('form/', calcularConsumo, name='form'),  
]
