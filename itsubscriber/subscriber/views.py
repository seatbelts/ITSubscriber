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
    serializer_class = ProyectoSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (ProyectoPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Proyecto.objects.all()
        return Proyecto.objects.filter(equipo__usuario=self.request.user)


class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AlumnoPermission, )


class EquipoViewSet(ModelViewSet):
    serializer_class = EquipoSerializer
    # authentication_classes = (TokenAuthentication, )
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
    serializer_class = MaestroSerializer

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

'''
Endpoint to create new users
'''


class CreateUserView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
