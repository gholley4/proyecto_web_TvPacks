from django.db import models

# Create your models here.
opciones_region = [('1', 'Metropolitana'), ('2', 'Coquimbo'), ('3', 'Maule'), ('4', 'Araucania')]
opciones_tipo_pack = [('1', 'ORO HD'), ('2', 'PLATA HD'), ('3', 'BRONCE HD'), ('4', 'ORO 4K'), ('5', 'PLATA 4K'), ('6', 'BRONCE 4K')]


class Cliente(models.Model):
        nombre = models.CharField(max_length=50)
        rut = models.CharField(max_length=10)
        email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
        telefono = models.IntegerField()
        region = models.CharField(max_length=30, choices=opciones_region)
        fecha_nacimiento = models.DateField()
        tipo_pack = models.CharField(max_length=50, choices=opciones_tipo_pack)        

        def __str__(self):
            return self.nombre
