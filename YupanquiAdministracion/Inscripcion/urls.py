from django.urls import path
from .views import  Busqueda, BuscarSocio, CrearIncripcion, InscripcionDetailView, EditarInscripcion, EliminarInscripcion

urlpatterns = [

    path('', BuscarSocio.as_view(), name='index_inscripcion'),  
       
    path('inscribir/<int:socio_id>', CrearIncripcion.as_view(), name='inscripcion'),
    
    path('detalle_inscripcion/<int:socio_id>', InscripcionDetailView.as_view(), name='detalle_inscripcion'),

    path('editar-inscripcion/<int:pk>', EditarInscripcion.as_view(), name='editar_inscripcion'),
    path('eliminar_inscripcion/<int:pk>', EliminarInscripcion.as_view(), name='eliminar_inscripcion'),

    path('busqueda/',Busqueda.as_view(), name='busqueda')
]