# Generated by Django 4.1.1 on 2022-10-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
