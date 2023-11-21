from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Socio
from .forms import SocioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import  UserPassesTestMixin
from django.contrib import messages
# Create your views here.

class BuscarSocioView(LoginRequiredMixin,ListView):
    model = Socio
    template_name = 'socios/index_socios.html'
    context_object_name = 'socios'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query) | Socio.objects.filter(dni__icontains=query)
        return Socio.objects.all()
    
class DetalleSocio(LoginRequiredMixin,DetailView):
   
    model = Socio
    context_object_name = 'detalle_socio'
    context_object_name = 'socio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar las inscripciones asociadas al contexto
        context['inscripciones'] = self.object.inscripciones.all()
        return context
  

class CrearSocio(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Socio   
    form_class = SocioForm
    template_name = 'socios/crear_socio.html'
    success_url = reverse_lazy('index_socios')

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):
        # Puedes agregar lógica adicional antes de guardar el formulario, si es necesario
        messages.success(self.request, 'Socio registrado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Puedes agregar lógica adicional para manejar el caso cuando el formulario no es válido
        messages.error(self.request, 'Error al registrar Socio. Por favor, revise los campos.')
        return super().form_invalid(form)

class EditarSocio(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Socio
    form_class= SocioForm
    template_name = 'socios/editar_socio.html'  
    success_url = reverse_lazy("index_socios")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):
        # Puedes agregar lógica adicional antes de guardar el formulario, si es necesario
        messages.success(self.request, 'Socio modificado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Puedes agregar lógica adicional para manejar el caso cuando el formulario no es válido
        messages.error(self.request, 'Error al modificar el Socio. Por favor, revise los campos.')
        return super().form_invalid(form)



class EliminarSocio(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Socio
    template_name = 'socios/eliminar_socio.html'
    success_url = reverse_lazy("index_socios")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')


