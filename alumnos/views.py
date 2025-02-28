from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .models import Alumno

from .forms import *

from .serializers import AlumnoSerializer

# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]

def vista_alumnos(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlumnoForm()  # Asegurar que 'form' esté definido en solicitudes GET

    return render(request, 'alumnos.html', {'form': form})
