from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

from django.shortcuts import  render
from .forms import productoForm

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    renderer_classes = [JSONRenderer]



def agregar_view(request):
    form = productoForm()
    return render(request,'agregar.html',{'form':form})