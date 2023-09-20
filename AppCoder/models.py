from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - Comisión: {self.comision}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True , blank=True)

class Profesores(models.Model):
    nombre = models.CharField(max_length=60)
    materia = models.CharField(max_length=60)
   