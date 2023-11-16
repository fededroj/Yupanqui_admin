from django.contrib import admin
#admin de modelos
from .models import *
from Socios.models import Socio
from Cuotas.models import CuotaMensual, CuotaActividad
from Inscripcion.models import Inscripcion




# Register your models here.
admin.site.register(Socio)
admin.site.register(Inscripcion)
admin.site.register(Actividad)
admin.site.register(Categoria)
admin.site.register(CuotaMensual)
admin.site.register(CuotaActividad)

