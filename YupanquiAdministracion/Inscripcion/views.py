from django.shortcuts import redirect
from.models import Inscripcion
from Socios.models import Socio
from.forms import InscripcionForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView 
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
# Create your views here.


class BuscarSocio(ListView):
    model = Socio
    template_name = 'inscripcion/buscar.html'
    context_object_name = 'socios'
    
  

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query) | Socio.objects.filter(nombre__icontains=query)
        return Socio.objects.all()
    
class CrearIncripcion(LoginRequiredMixin,UserPassesTestMixin,CreateView): 
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'inscripcion/crear_inscripcion.html'
    success_url= reverse_lazy("index_socios")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')

    def get_initial(self):
      #  Obtiene el ID del socio desde la URL (debes configurar la URL en consecuencia)
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}
    
    def form_valid(self, form):
        # Puedes agregar lógica adicional antes de guardar el formulario, si es necesario
        messages.success(self.request, 'Inscripción creada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Puedes agregar lógica adicional para manejar el caso cuando el formulario no es válido
        messages.error(self.request, 'Error al crear la inscripción. Por favor, revise los campos.')
        return super().form_invalid(form)

class InscripcionDetailView(LoginRequiredMixin,DetailView):   
    model = Inscripcion
    template_name='socios/socio_detail.html'
    context_object_name = 'inscripcion'
     
    def get_object(self, queryset=None):
        # Utiliza el campo nroSocio en lugar de la PK
        return self.model.objects.get(nroSocio=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la instancia de Socio asociada a la Inscripcion
        context['socio_instance'] = self.object.socio
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Puedes agregar más contexto si lo necesitas
    #     return context


class EditarInscripcion(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Inscripcion
    form_class= InscripcionForm
    template_name = 'inscripcion/editar_inscripcion.html'  
    success_url = reverse_lazy("index_socios")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def form_valid(self, form):
        # Puedes agregar lógica adicional antes de guardar el formulario, si es necesario
        messages.success(self.request, 'Inscripción modificada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Puedes agregar lógica adicional para manejar el caso cuando el formulario no es válido
        messages.error(self.request, 'Error al modificar la inscripción. Por favor, revise los campos.')
        return super().form_invalid(form)
    
   

class EliminarInscripcion(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Inscripcion
    template_name = 'inscripcion/inscripcion_delete.html'
    success_url = reverse_lazy("index_socios")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
