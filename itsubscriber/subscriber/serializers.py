from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from .models import *

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        exclude = ()

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        exclude = ()

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        exclude = ()

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        exclude = ()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()

        return user
    class Meta:
        model = User
        fields = ('username','password' ,'first_name', 'last_name', 'email', 'id',)




