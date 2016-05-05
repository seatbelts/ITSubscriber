from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from subscriber.views import *

router = DefaultRouter()
router.register(r'eventos', EventoViewSet, 'evento')
router.register(r'proyectos', ProyectoViewSet, 'proyecto')
router.register(r'equipos', EquipoViewSet, 'equipo')
router.register(r'alumnos', AlumnoViewSet, 'alumno')
router.register(r'usuarios', UserViewSet, 'user')
router.register(r'materias', MateriaViewSet, 'materia')
router.register(r'maestros', MaestroViewSet, 'maestro')
router.register(r'categorias', CategoriasViewSet, 'categorias')
# router.register(r'register', CreateUserView.as_view(), base_name='register')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^login/', ObtainAuthToken.as_view()),
    url(r'^register/', CreateUserView.as_view()),
]


