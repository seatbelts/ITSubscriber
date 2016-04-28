from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return '%s' %self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    maestro = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s' %(self.nombre, self.maestro)

def file_name(instance, filename):
    return '/'.join([instance.evento.nombre, instance.nombre, filename])

class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    materia = models.ManyToManyField(Materia)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    mesa = models.CharField(max_length=3, null=True)
    archivo = models.FileField(null=True, upload_to=file_name)

    def __str__(self):
        return '%s' %self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    matricula = models.PositiveIntegerField(primary_key=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%d - %s' %(self.matricula, self.nombre)

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.OneToOneField(Proyecto)
    lider = models.ForeignKey(Alumno, related_name='lider')
    integrantes = models.ManyToManyField(Alumno, related_name='integrantes')

    def __str__(self):
        return '%s - Lider: %s' %(self.nombre, self.lider.nombre)


