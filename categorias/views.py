from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Categoria
from .forms import categoryForm


# Create your views here.


#para consumo de api
def lista_categorias (request):
    categorias = Categoria.objects.all()

    #dict parse

    data = [
        {
            'nombre':c.nombre,
            'imagen':c.imagen

        }
        for c in categorias

    ]
    return JsonResponse(data,safe=False)

def ver_categorias(request):
    return render(request,'ver_categorias.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = categoryForm
    return render(request,'agergar_categoria.html',{'form':form})