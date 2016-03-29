from django.db import models
from django.contrib.auth.models import User

MATERIAS = (
    ('IHC', 'Interaccion Humano Computadora'),
    ('DM', 'Dispositivos Moviles'),
    ('CI', 'Computo Integrado'),
)

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return '%s' %self.nombre

class Projecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    materia = models.CharField(choices=MATERIAS, max_length=5)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    mesa = models.CharField(max_length=3)

    def __str__(self):
        return '%s' %self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    matricula = models.PositiveIntegerField(primary_key=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%d - %s' %(self.matricula, self.nombre)

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.OneToOneField(User)
    lider = models.OneToOneField(Alumno, related_name='lider')
    integrantes = models.ManyToManyField(Alumno, related_name='integrantes')

    def __str__(self):
        return '%s - Lider: %s' %(self.nombre, self.lider.nombre)


