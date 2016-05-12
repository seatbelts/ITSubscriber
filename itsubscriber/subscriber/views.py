from rest_framework import status, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .serializers import *
from .permissions import *


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (EventoPermission, )

from pprint import pprint
class ProyectoViewSet(ModelViewSet):
    queryset = Proyecto.objects.all()
    # serializer_class = ProyectoSerializer
    # permission_classes = (ProyectoPermission, )

    def get_queryset(self):
        pprint(self.request.user.id)
        if self.request.user.is_staff:
            return Proyecto.objects.all()
        elif self.request.user.is_authenticated():
            return Proyecto.objects.filter(equipo__integrantes=self.request.user.username)
        else:
            return False

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProyectoDataSerializer
        else:
            return ProyectoSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (AlumnoPermission, )


class EquipoViewSet(ModelViewSet):
    serializer_class = EquipoSerializer
    permission_classes = (EquipoPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Equipo.objects.all()
        return Equipo.objects.filter(usuario=self.request.user)


class MateriaViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (MateriaPermission, )


class MaestroViewSet(ModelViewSet):
    queryset = Maestro.objects.all()
    # serializer_class = MaestroSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MaestroDataSerializer
        else:
            return MaestroSerializer


class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

'''
Endpoint to create new users
'''


class CreateUserView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        alumno = serializer.data
        student = Alumno(
            nombre=alumno['first_name'],
            apellidos=alumno['last_name'],
            correo=alumno['email'],
            telefono=self.request.data['telefono'],
            matricula=int(alumno['username']),
            user=User.objects.get(id=alumno['id']))
        student.save()


from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer


class ObtainAuthToken(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            role = 'admin' if user.is_staff else 'user'
            response_data['first_name'] = user.first_name
            response_data['last_name'] = user.last_name
            response_data['email'] = user.email
            response_data['username'] = user.username
            response_data['role'] = role
            response_data['id'] = user.id

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefreshAuthToken(ObtainAuthToken):

    serializer_class = RefreshJSONWebTokenSerializer
