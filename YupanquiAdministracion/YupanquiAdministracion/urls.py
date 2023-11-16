"""
URL configuration for YupanquiAdministracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from Usuarios.views import LoginFormView
from django.contrib.auth.decorators import login_required
from Administracion.views import ErrorView


urlpatterns = [
 
    path('admin/', admin.site.urls),    
    path('lagout/',auth_views.LogoutView.as_view(template_name='accounts/login/'), name='lagout'),
    
    path('', include("Socios.urls")),    
    path('administracion/',include("Administracion.urls")), 
    path('cuotas/', include("Cuotas.urls")),
    path('inscripcion/', include("Inscripcion.urls")) , 
    path('accounts/', include("django.contrib.auth.urls")),
    
    path('error/',login_required(ErrorView.as_view()),name='error_permiso')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)