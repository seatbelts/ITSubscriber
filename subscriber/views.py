from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import *
from .serializers import *

class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ProyectoViewSet(ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

