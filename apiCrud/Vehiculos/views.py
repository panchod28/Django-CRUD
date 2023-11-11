from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.urls import reverse
import base64
from PIL import Image
from io import BytesIO

from Vehiculos.models import Vehiculos
from Vehiculos.serializers import VehiculosSerializer

# Vistas de la API

@csrf_exempt
def vehiculosApi(request, id=0):
    if request.method == 'GET':
        vehiculos = Vehiculos.objects.all()
        vehiculos_serializer = VehiculosSerializer(vehiculos, many=True)
        return JsonResponse(vehiculos_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        vehiculos_serializer = VehiculosSerializer(data=data)
        if vehiculos_serializer.is_valid():
            vehiculos_serializer.save()
            vehiculos = Vehiculos.objects.all()  # Obtener la lista actualizada de vehiculos
            return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})
        return JsonResponse("Error al guardar vehiculo", safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        vehiculo = Vehiculos.objects.get(VehiculoId=data['VehiculoId'])
        vehiculos_serializer = VehiculosSerializer(vehiculo, data=data)
        if vehiculos_serializer.is_valid():
            vehiculos_serializer.save()
            vehiculos = Vehiculos.objects.all()  # Obtener la lista actualizada de vehiculos
            return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})
        return JsonResponse("Error al actualizar")
    elif request.method == 'DELETE':
        vehiculo = Vehiculos.objects.get(VehiculoId=id)
        vehiculo.delete()
        vehiculos = Vehiculos.objects.all()  # Obtener la lista actualizada de vehiculos
        return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})


# Vistas del formulario

def formulario_vehiculo(request):
    if request.method == 'POST':
        data = request.POST
        vehiculos_serializer = VehiculosSerializer(data=data)
        if vehiculos_serializer.is_valid():
            vehiculos_serializer.save()
            return redirect('lista_vehiculos')
    return render(request, 'formulario.html')

""" def agregar_facultad(request):
    if request.method == 'POST':
        data = request.POST
        facultades_serializer = FacultadesSerializer(data=data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            #facultades = Facultades.objects.all()  # Obtener la lista actualizada de facultades
            #return render(request, 'lista_facultades.html', {'facultades': facultades})
            return redirect(reverse('facultadesApi'))
    return render(request, 'formulario.html') """

def agregar_vehiculo(request):
    if request.method == 'POST':
        data = request.POST
        imagen = request.FILES.get('imagen')  # Asegúrate de que 'imagen' sea el nombre correcto del campo de archivo en tu formulario

        # Actualiza la instancia del serializador con la imagen
        vehiculos_serializer = VehiculosSerializer(data=data)
        if vehiculos_serializer.is_valid():
            if imagen:
                with Image.open(imagen) as img:
                    buffered = BytesIO()
                    img.save(buffered, format="JPEG")
                    imagen_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
                    vehiculos_serializer.validated_data['imagen'] = imagen_base64

            vehiculo = vehiculos_serializer.save()
            return redirect('lista_vehiculos')  # Redirigir a la vista lista_vehiculos
        else:
            return JsonResponse(vehiculos_serializer.errors, status=400)
    else:
        return render(request, 'formulario.html')
    


def lista_vehiculos(request):
    vehiculos = Vehiculos.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

def editar_vehiculo(request, id):
    vehiculo = Vehiculos.objects.get(VehiculoId=id)
    
    if request.method == 'POST':
        vehiculo.identificador = request.POST.get('identificador', '')
        vehiculo.tipo = request.POST.get('tipo', '')
        vehiculo.modelo = request.POST.get('modelo', '')
        vehiculo.marca = request.POST.get('marca', '')
        vehiculo.ano = request.POST.get('ano', '')
        vehiculo.descripcion = request.POST.get('descripcion', '')
        vehiculo.valorDia = request.POST.get('valorDia', '')
        vehiculo.estado = request.POST.get('estado', '')
        
        imagen = request.FILES.get('imagen')
        if imagen:
            # Procesar la imagen y guardarla como una cadena base64 en el campo imagen
            with Image.open(imagen) as img:
                buffered = BytesIO()
                img.save(buffered, format="JPEG")
                imagen_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
                vehiculo.imagen = imagen_base64
        elif not vehiculo.imagen:
            # Si la nueva imagen es vacía y no hay una imagen existente, mantener el valor existente
            vehiculo.imagen = vehiculo.imagen

        vehiculo.save()
        return redirect('lista_vehiculos')
    else:
        return render(request, 'editar_vehiculo.html', {'vehiculo': vehiculo})

def eliminar_vehiculo(request, id):
    if request.method == 'POST':
        vehiculo = Vehiculos.objects.get(VehiculoId=id)  
        vehiculo.delete()
    return redirect('lista_vehiculos')

