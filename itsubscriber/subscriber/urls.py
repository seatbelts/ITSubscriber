from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'usuarios', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
