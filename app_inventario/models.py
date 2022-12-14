from django.db import models
from django.utils import timezone
from dateutil import relativedelta
from datetime import datetime
# Create your models here.
class Inventarios(models.Model):
    id = models.AutoField(primary_key=True)
    FechaInventario = models.DateField()
    GLN_Cliente = models.CharField(max_length=100)
    GLN_Sucursal = models.CharField(max_length=100)
    Gtin_Producto = models.CharField(max_length=100)
    Inventario_Final = models.IntegerField(null=True)
    PrecioUnidad = models.IntegerField()

    def diff_on_time(self):
        now = timezone.now().date()
        if self.FechaInventario:
            diff =relativedelta.relativedelta(now, self.FechaInventario)
            return str(diff)


    def __str__(self):
        return self.GLN_Cliente

class Cliente(models.Model):
    GLN_Cliente = models.CharField(max_length=100)
    def __str__(self):
        return self.GLN_Cliente

class Sucursal(models.Model):
    GLN_Sucursal = models.CharField(max_length=100)
    def __str__(self):
        return self.GLN_Sucursal

class Producto(models.Model):
    Gtin_Producto = models.CharField(max_length=100)
    def __str__(self):
        return self.Gtin_Producto