from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


def file_name(instance, filename):
    return '/'.join([instance.evento.nombre, instance.nombre, filename])

'''
Abstract model
'''


class PersonalData(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = True


class Evento(TimeStampedModel, models.Model ):
    nombre = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nombre)


class Maestro(PersonalData):
    materia = models.ForeignKey(Materia, null=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    materia = models.ManyToManyField(Materia)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    mesa = models.CharField(max_length=3, null=True)
    archivo = models.FileField(null=True, upload_to=file_name)

    def __str__(self):
        return '%s' % self.nombre


class Alumno(PersonalData):
    matricula = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return '%d - %s' % (self.matricula, self.nombre)


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.OneToOneField(Proyecto)
    lider = models.ForeignKey(Alumno, related_name='lider')
    integrantes = models.ManyToManyField(Alumno, related_name='integrantes')

    def __str__(self):
        return '%s - Lider: %s' % (self.nombre, self.lider.nombre)
