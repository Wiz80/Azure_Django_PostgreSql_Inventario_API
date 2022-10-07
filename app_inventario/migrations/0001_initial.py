# Generated by Django 4.1.1 on 2022-10-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GLN_Cliente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaInventario', models.DateField()),
                ('GLN_Cliente', models.CharField(max_length=100)),
                ('GLN_Sucursal', models.CharField(max_length=100)),
                ('Gtin_Producto', models.CharField(max_length=100)),
                ('Inventario_Final', models.IntegerField(null=True)),
                ('PrecioUnidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gtin_Producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GLN_Sucursal', models.CharField(max_length=100)),
            ],
        ),
    ]