from django.urls import path
from Vehiculos import views
from django.contrib import admin
from Vehiculos.views import eliminar_vehiculo, lista_vehiculos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculo/', views.vehiculosApi),
    path('vehiculo/<int:id>/', views.vehiculosApi, name='vehiculo-detail'),
    
    path('vehiculo/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),

    path('vehiculo/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('vehiculos/', views.vehiculosApi, name='vehiculosApi'),
    path('lista_vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),


    path('formulario/', views.formulario_vehiculo, name='formulario_vehiculo'),    
]