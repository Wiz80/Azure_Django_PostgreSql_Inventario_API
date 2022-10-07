from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from app_inventario.serializer import InventarioSerializer
from app_inventario.models import Inventarios

class InventarioPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class InventarioList(ListAPIView):
    queryset = Inventarios.objects.all()
    serializer_class = InventarioSerializer
    filter_backends =(DjangoFilterBackend, SearchFilter)
    #filterset_fields = ['user__id','user__username']
    filter_fields = ('id')
    search_fields = ('GLN_Cliente')
    pagination_class = InventarioPagination

class InventarioCreate(CreateAPIView):
    serializer_class = InventarioSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('PrecioUnidad')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})

        except ValueError:
            raise ValidationError({'price':'Needs to be a number'})

        return super().create(request, *args, **kwargs)

class InventarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Inventarios.objects.all().all()
    lookup_field = 'id'
    serializer_class = InventarioSerializer

    def delete(self, request, *args, **kwargs):
        inventario_producto = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('inventario_data_{}'.format(inventario_producto))
        return response

    
    def update(self, request, *args, **kwargs):
        response = super().update(request,*args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            inventario = response.data
            cache.set('inventario_data_{}'.format(inventario['id']),{
                'FechaInventario' : inventario['FechaInventario'],
                'GLN_Cliente' : inventario['GLN_Cliente'], 
                'GLN_Sucursal' : inventario['GLN_Sucursal'],
                'Gtin_Producto' : inventario['Gtin_Producto'],
                'Inventario_Final' : inventario['Inventario_Final'],
                'PrecioUnidad' : inventario['PrecioUnidad']
            })
        return response
