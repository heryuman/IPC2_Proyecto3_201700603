from django.urls import path
from .views import index,cargar

urlpatterns = [
    path('', index,name='index'),
    path('cargar/',cargar,name='cargar'),
    #path('cargado/',cargado,name='cargado'),
]