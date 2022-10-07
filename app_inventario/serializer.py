from rest_framework import serializers

from app_inventario.models import Inventarios

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventarios
        fields = ('id','FechaInventario', 'GLN_Cliente', 'GLN_Sucursal', 'Gtin_Producto', 'Inventario_Final', 'PrecioUnidad')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['diff_time'] = instance.diff_on_time()
        return data