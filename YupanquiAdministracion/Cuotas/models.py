from django.db import models
from Socios.models import Socio
from Administracion.models import Actividad
from datetime import datetime, date

class CuotaMensual(models.Model):
    MES_CHOICES = (
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Sepiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
       
    )
    
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    mes = models.IntegerField(choices=MES_CHOICES)
    ano = models.IntegerField(default=datetime.now().year)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(default=date.today)
    mes_pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cuota de {self.get_mes_display()} {self.ano} - {self.socio}"
    class Meta:
        unique_together = ('socio', 'mes', 'ano') 
class CuotaActividad(models.Model):
    
    MES_CHOICES = (
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Sepiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
       
    )
    
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    mes = models.IntegerField(choices=MES_CHOICES)
    ano = models.IntegerField(default=datetime.now().year)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(default=date.today)

    def __str__(self):
        return f"Cuota de {self.get_mes_display()} {self.ano} - {self.socio} -{self.actividad}"
    
    class Meta:
        unique_together = ('socio', 'actividad', 'mes', 'ano') 

