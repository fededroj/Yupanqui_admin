
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static






urlpatterns =[
   
    path('',views.BuscarSocioView.as_view(),name='index_socios'),
    path('detalle_socio/<int:pk>', views.DetalleSocio.as_view(), name="detalle_socio"),
    path('crear_socio',views.CrearSocio.as_view(), name='crear_socio'),
    path('editar_socio/<int:pk>',views.EditarSocio.as_view(), name="editar_socio"),
    path('eliminar_socio/<int:pk>', views.EliminarSocio.as_view(), name="eliminar_socio"),  
    path('buscar',views.BuscarSocioView.as_view(), name="buscar_socio") , 

    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)