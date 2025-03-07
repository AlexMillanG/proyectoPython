from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import CustomUserSerializer
from .models import CustomUser

# Vista API REST
class UserViewSets(viewsets.ModelViewSet):  # Corregido aquí
    # Variables
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    # En caso de agregar seguridad
    # con las siguientes variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # Qué métodos hay que proteger
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

# Vista que devuelva token
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):  # Corregido aquí
    serializer_class = CustomTokenObtainPairSerializer