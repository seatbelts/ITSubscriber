from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from .models import *

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('url', 'id', 'nombre', 'description')

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('url', 'id', 'nombre', 'description', 'mesa', 'archivo', 'evento', 'categoria', 'materia',)

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('url', 'nombre', 'apellidos', 'correo', 'telefono', 'user', 'matricula')

class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo
        fields = ('url', 'id', 'nombre', 'usuario', 'proyecto', 'lider', 'integrantes')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('url', 'id', 'nombre')

class MaestroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maestro
        fields = ('url', 'id', 'nombre', 'apellidos', 'correo', 'telefono', 'materia' )

class CategoriasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorias
        fields = ('url', 'id', 'nombre')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
        
    class Meta:
        model = User
        fields = ('username','password' ,'first_name', 'last_name', 'email', 'id',)




