from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from subscriber.views import *

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'proyectos', ProyectoViewSet, base_name='proyecto')
router.register(r'equipos', EquipoViewSet, base_name='equipo')
router.register(r'alumnos', AlumnoViewSet)
router.register(r'usuarios', UserViewSet, base_name='usuario')
router.register(r'materias', MateriaViewSet)
router.register(r'maestros', MaestroViewSet)
# router.register(r'register', CreateUserView.as_view(), base_name='register')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.obtain_auth_token),
    url(r'^register/', CreateUserView.as_view()),
]
