from django.db import models

class ReporteVial (models.Model):
    numdeticket = models.CharField(max_length=15)
    tiempo_evento = models.DateTimeField()
    motivo = models.CharField(max_length=50)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True,blank=True)
    def __str__(self):
        return self.numdeticket

