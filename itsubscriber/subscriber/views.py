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


class ProyectoViewSet(ModelViewSet):
    queryset = Proyecto.objects.all()
    # serializer_class = ProyectoSerializer
    # permission_classes = (ProyectoPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Proyecto.objects.all()
        return Proyecto.objects.filter(equipo__integrantes=self.request.user)

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

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        role = 'admin' if user.is_staff else 'user'
        return Response({
            'token': token.key,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'role': role,
            'id': user.id
        })
