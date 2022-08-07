from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import yaml
import os
from azure.storage.blob import ContainerClient
import pandas as pd
import numpy as np
import copy
from datetime import datetime

from inventario_app.models import Inventario, Cliente, Sucursal, Producto


# Create your views here.

def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open(dir_root + "/config.yaml", "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)

def upload(file, connenction_string, container_name):
    container_client = ContainerClient.from_connection_string(connenction_string, container_name)
    print("uploading file to blob storage ...")
    
    data = pd.read_csv(file, header=0)
    name = data['GLN_Cliente'][0]
    random_value = np.random.randint(0, 100000000)
    blob_client = container_client.get_blob_client(f'{name}/{name}_{random_value}.csv')    
    data_to_csv = copy.deepcopy(data)
    output = data_to_csv.to_csv(index=None)
    blob_client.upload_blob(output, blob_type="BlockBlob")

    data['FechaInventario'] = pd.to_datetime(data['FechaInventario'])
    for idx, i in data.iterrows():
        inventario = Inventario.objects.create(
            FechaInventario = i['FechaInventario'],
            GLN_Cliente = i['GLN_Cliente'],
            GLN_Sucursal = i['GLN_Sucursal'],
            Gtin_Producto = i['Gtin_Producto'],
            Inventario_Final = i['Inventario_Final'],
            PrecioUnidad =  i['PrecioUnidad']
        )        
        inventario.save()
        if len(Cliente.objects.filter(GLN_Cliente = i['GLN_Cliente'])) == 0:
            cliente = Cliente.objects.create(GLN_Cliente = i['GLN_Cliente'])
            cliente.save()
        if len(Sucursal.objects.filter(GLN_Sucursal = i['GLN_Sucursal'])) == 0:
            sucursal = Sucursal.objects.create(GLN_Sucursal = i['GLN_Sucursal'])
            sucursal.save()
        if len(Producto.objects.filter(Gtin_Producto = i['Gtin_Producto'])) == 0:
            producto = Producto.objects.create(Gtin_Producto = i['Gtin_Producto'])            
            producto.save()
    
def index(request):
    if request.method == 'POST':
        file_name = request.FILES.get('file')
        file = request.FILES['file']
        config = load_config()
        upload(file, config['azure_storage_connectionstring'], config['inventario_container_name'])
        
        return render(request,
                      'base/index.html',
                      {'file_name': file_name})

    return render(request,
                 'base/index.html')


"""
def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startwith('.'):
                yield entry
"""