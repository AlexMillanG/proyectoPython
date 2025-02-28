from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .models import Alumno

from .serializers import AlumnoSerializer

# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]