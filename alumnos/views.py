from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .forms import AlumnoForm
from .serializers import AlumnoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]

def vista_alumnos(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('id')

        if alumno_id:  # Si hay un ID, actualizar en lugar de crear
            alumno = get_object_or_404(Alumno, id=alumno_id)
            form = AlumnoForm(request.POST, instance=alumno)
        else:  # Si no hay ID, crear uno nuevo
            form = AlumnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vista_alumnos')  # Redirigir para evitar reenvíos duplicados

    else:
        form = AlumnoForm()  # Asegurar que 'form' esté definido en solicitudes GET

    return render(request, 'alumnos.html', {'form': form})
