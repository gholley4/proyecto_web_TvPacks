from django.db import models

# Create your models here.

class Cliente(models.Model):
        nombre = models.CharField(max_length=50)
        rut = models.CharField(max_length=10)
        email = models.CharField(max_length=50)
        telefono = models.IntegerField()
        region = models.CharField(max_length=30)
        fecha_nacimiento = models.DateField()
        tipo_pack = models.CharField(max_length=20)        

        def __str__(self):
            return self.nombre
