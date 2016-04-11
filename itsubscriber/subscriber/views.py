from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
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
    authentication_classes = (TokenAuthentication, )
    permission_classes = (EventoPermission, )

class ProyectoViewSet(ModelViewSet):
    serializer_class = ProyectoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (ProyectoPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Proyecto.objects.all()
        return Proyecto.objects.get(equipo__usuario=self.request.user)

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AlumnoPermission, )

class EquipoViewSet(ModelViewSet):
    serializer_class = EquipoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (EquipoPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Equipo.objects.all()
        return Equipo.objects.get(usuario=self.request.user)

class MateriaViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (MateriaPermission, )

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UserPermission, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.get(id=self.request.user.id)
