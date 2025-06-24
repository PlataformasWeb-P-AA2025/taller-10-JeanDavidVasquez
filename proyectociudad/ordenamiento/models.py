from django.db import models

# Create your models here.

#Dadas dos entidades:

#Parroquia:

#- nombre
#- ubicación (norte, sur, este, oeste)
#- tipo [urbana, rural]

#Barrio o Ciudadela:

#- nombre
#- número de viviendas
#- número de parques [1, 2, 3, 4, 5, 6]
#- número de edificios residenciales
#- parroquia

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50)  # norte, sur, este, oeste
    tipo = models.CharField(max_length=10, choices=[('urbana', 'Urbana'), ('rural', 'Rural')])

    def __str__(self):
        return self.nombre
    
class BarrioCiudadela(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])  # 1 a 6 parques
    numero_edificios_residenciales = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre