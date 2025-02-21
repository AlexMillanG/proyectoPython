import json

from django.shortcuts import render, redirect
from .models import Producto

from django.http import JsonResponse
from .forms import productoForm
# Create your views here.


def lista_productos(request):
    #bd findAll
    productos = Producto.objects.all()

    #parsear datos a un dict

    data=[
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen':p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request,'ver.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            #guarda en db
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    return render(request,'agregar.html',{'form':form})


# Función que agrega un producto con un objeto JSON
def registrar_producto(request):
    # Checar si nuestra request es de tipo POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parámetro es un texto que debería ser un JSON
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )
            # create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': producto.id
                },
                status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)}, status=400)

    # Si no es POST el request...
    return JsonResponse({'error': 'El método no está soportado'}, status=405)
