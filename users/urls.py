from django.urls import path, include  # Corregido: importar include desde django.urls
from django.contrib.auth.views import LogoutView

from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

# Configuración del router
router = SimpleRouter()
router.register(r'api', UserViewSets)  # Registrar la vista UserViewSets

urlpatterns = [
    # Rutas de autenticación
    # path('register/', register_view, name='register'),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('home/', home_view, name='home'),

    # Rutas para JWT
    #path login
    #requiere email y password solo funciona con POST
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),  # Ruta para obtener el token
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),  # Ruta para refrescar el token

    # Incluir las rutas del router
    path('', include(router.urls)),  # Corregido: incluir router.urls directamente
]