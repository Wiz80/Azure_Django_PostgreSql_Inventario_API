from django.urls import path
from . import views, api_views

urlpatterns = [
    path('api/inventario/', api_views.InventarioList.as_view()),
    path('api/inventario/new', api_views.InventarioCreate.as_view()),
    path('api/inventario/<int:id>/',
        api_views.InventarioRetrieveUpdateDestroy.as_view(),
    ),
    path('', views.index, name='index')
]