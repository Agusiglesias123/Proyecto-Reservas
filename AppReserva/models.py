from django.db import models

# Create your models here.


class Sectores(models.Model):
    sector = models.CharField(max_length=20)

    class Meta:
        verbose_name='sector'
        verbose_name_plural='sectores'

    def __str__(self):
        return '{}' .format(self.sector)

class Timer(models.Model):
    time = models.CharField(max_length=20)

    class Meta: 
        verbose_name='hora'
        verbose_name_plural='horas'

    def __str__(self):
        return '{}' .format(self.time)



class Reserva(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=50)
    sector = models.ForeignKey(Sectores, null = True, blank= True,on_delete=models.CASCADE)
    comensales = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.ForeignKey(Timer, null = True, blank= True, on_delete=models.CASCADE)

    class Meta:
        verbose_name='reserva'
        verbose_name_plural='reservas'

    def __str__(self):
        return '{}'.format(self.nombre)