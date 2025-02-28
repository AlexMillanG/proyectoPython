
from .views import *
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'api', AlumnoViewSet)

urlpatterns = [
    path('',include(router.urls))
]