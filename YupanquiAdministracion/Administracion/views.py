from typing import Any
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Profesor, Actividad, Categoria
from .forms import ProfesorForm, ActividadForm, CategoriaForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView 
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
import os
from django.conf import settings
from django.contrib import messages



#   VISTA DE ERROR DE PERMISOS

class ErrorView(LoginRequiredMixin,TemplateView):
    template_name='error_permiso.html'

    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)
       error_image_path = os.path.join(settings.MEDIA_URL,'imagenes/error.png')
       context['error_image_path']= error_image_path
       return context


# class Index(LoginRequiredMixin,TemplateView):
#     def get(self, request ,*args,**kwargs):
#         return render(request, "administracion/index.html")



#                                  Profesor

#   CREAR INDEX LISTA PROFESORES
class ProfesoresListView(LoginRequiredMixin,ListView):
    model = Profesor
    paginate_by = 15
    context_object_name = 'profesores'
    template_name = 'administracion/profesores.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Profesor.objects.filter(nombre__icontains=query) | Profesor.objects.filter(apellido__icontains=query)
        return Profesor.objects.all()
    
#   DETALLE DE PROFESOR    
class DetalleProfesor(LoginRequiredMixin,DetailView):
    model = Profesor
    context_object_name = 'detalle_profesor'


    
#   CREAR NUEVO PROFESOR
class CrearProfesor(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Profesor   
    form_class = ProfesorForm
    template_name = 'administracion/crear_profesor.html'
    success_url = reverse_lazy('lista_profesores')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')

    def form_valid(self, form):        
        messages.success(self.request, 'Profesor agregado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):        
        messages.error(self.request, 'Error al crear el Profesor. Por favor, revise los campos.')
        return super().form_invalid(form)
class EditarProfesor(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Profesor
    form_class= ProfesorForm
    template_name = 'administracion/editar_profesor.html'  
    success_url = reverse_lazy("lista_profesores")
    
    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):        
        messages.success(self.request, 'Profesor modificado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):    
        messages.error(self.request, 'Error al modificiar el Profesor. Por favor, revise los campos.')
class EliminarProfesor(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Profesor
    template_name = 'administracion/eliminar_profesor.html'
    success_url = reverse_lazy('lista_profesores')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')


                                       #ACTIVIDADES

class ActividadesListView(LoginRequiredMixin,ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'administracion/actividades.html'    

class DetalleActividad(LoginRequiredMixin,DetailView):
    model= Actividad
    context_object_name= 'actividad'

class CrarActividad(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    
    model=Actividad
    form_class = ActividadForm
    template_name = 'administracion/crear_actividad.html'      
    success_url = reverse_lazy('lista_actividades')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')

    def form_valid(self, form):        
        messages.success(self.request, 'Actividad creada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):    
        messages.error(self.request, 'Error al crear la Actividad. Por favor, revise los campos.')
class EditarActividad(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Actividad
    form_class= ActividadForm
    template_name = 'administracion/editar_actividad.html'  
    success_url = reverse_lazy('lista_actividades')
    
    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):        
        messages.success(self.request, 'Actividad modificada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):    
        messages.error(self.request, 'Error al modificiar la Actividad. Por favor, revise los campos.')

class EliminarActividad(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Actividad
    template_name = 'administracion/eliminar_actividad.html'
    success_url = reverse_lazy('lista_actividades')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')


                         #Categorias
class CategoriasListView(LoginRequiredMixin,ListView):
    model = Categoria
    paginate_by = 15
    context_object_name="categorias"
    template_name = 'administracion/categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
class DetalleCategoria(LoginRequiredMixin,DetailView):
    model= Categoria
    context_object_name= 'detalle_categoria'
   
class CrearCategoria(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = 'administracion/crear_categoria.html'  
    success_url =reverse_lazy("lista_categorias")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):        
        messages.success(self.request, 'Categoria creada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):    
        messages.error(self.request, 'Error al crear la Categoria. Por favor, revise los campos.')
class EditarCategoria(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = 'administracion/editar_categoria.html'  
    success_url = reverse_lazy('lista_categorias')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):        
        messages.success(self.request, 'Categoria modificada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):    
        messages.error(self.request, 'Error al modificiar la Categoria. Por favor, revise los campos.')
   
class EliminarCategoria(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Categoria
    template_name = 'administracion/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
