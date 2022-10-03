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

## :exclamation: I have problems connecting my Azure web service to the Azure postgreSQL server, I get
```shell
failed: FATAL:  password authentication failed for user "azure_user"
connection to server at "msdocs-python-postgres-webapp-db-2680.postgres.database.azure.com" (13.86.36.172), port 5432 failed: FATAL:  no pg_hba.conf entry for host "20.84.233.39", user "azure_user", database "inventario", SSL off
```
Could you please help me?
I tried already add the Ipv4 address of the ssh shell of Azure Web Service to the networks allowed by the PostgreSQL database server and allowed all the ip addresses `+ Add 0.0.0.0 - 255.255.255.255` but it doesn't work
![image](https://user-images.githubusercontent.com/50804224/193678069-563dca3b-f99e-4a25-b3b4-6b6c398f8a3d.png)