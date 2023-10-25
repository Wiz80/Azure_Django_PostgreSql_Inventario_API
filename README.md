# Inventory API with Django, PostgreSQL and Azure 

This API was developed using the tutorial given in `Microsoft Learn` <a href="https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cazure-portal-access%2Cvscode-aztools-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions--zip-azcli%2Cdeploy-instructions-curl-bash">Here</a>

Instead of making 
```git
git clone https://github.com/Azure-Samples/djangoapp
```
You can use
```git
git clone https://github.com/Wiz80/Azure_Django_PostgreSql_Inventario_API.git
```
## What This Project is about?

![image](https://user-images.githubusercontent.com/50804224/193666851-2484ef4d-ec4c-4807-a2bc-2f79bea0874d.png)
<br>

It is requested to develop a system in which the user by means of a flat file (.csv) uploads an inventory template to a 🐲`PostgreSQL DB`. It should be noted that the file must first be uploaded to a :herb: `BlobStorage of Azure` and after its upload the data must be created or updated in the model of the DB in the corresponding case in order to have a loading and processing log of the same.

## Instructions :rocket:

### 1. Follow the `first step` of the Microsoft tutorial instructions   

:exclamation: Don't forget to change the `.env` file to connect your postgreSQL local database :exclamation:

When running:
```shell
python manage.py runserver
```
You will see a web page like this:
![image](https://user-images.githubusercontent.com/50804224/193666454-06d260dc-4f8f-4604-8f99-46c2861b564b.png)

You can download this inventory <a href="https://docs.google.com/spreadsheets/d/19aRZj6k9Zk2dsgCURbaGY3ykRd8d9iHECSp7oCGlvgQ/edit?usp=sharing">Test document</a>

##### Please, don't upload your .csv file until you change your `config.yaml` file in your `inventario_app` directory, you could change this file following <a href="https://www.youtube.com/watch?v=enhJfb_6KYU&t=354s"> this tutorial </a>  

### 2. When you have already change the config.yaml file and run the server again and upload the .csv file, you could go to your Containers in Azure Storage
![image](https://user-images.githubusercontent.com/50804224/193676320-e32dafba-b855-4926-94d2-63d4ac8d3ea5.png)

### 3. In your `inventario` container you will have a folder for all the clients in the .csv file that you upload
![image](https://user-images.githubusercontent.com/50804224/193676730-cb3c7315-49bb-48bb-8cbb-58c58b01032d.png)

### 4. Follow the next Microsoft tutorial instructions

## RestAPI

You'll find the `JSON serializer` for the inventory model extracted from the postgreSQL database, running the next url:

`/api/inventario/`

### :maple_leaf: Filters
You also have a filter system in the API view that you can change in the `InventarioList` class from the `app_inventario/api_views.py` file 

### :leaves: Retrieve Update Destroy

You can retrieve an inventory model whit 

`/api/inventario/<int:id>/`

You'll have a view where you can Update or delete the inventory object 
![image](https://user-images.githubusercontent.com/50804224/194674469-235fafcd-a51f-4799-8e30-b740601b88d4.png)

### :fallen_leaf: New object

Runnin the bellow url you could add new inventory object to deploy testing:

`/api/inventario/new/` 
