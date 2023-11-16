from django.shortcuts import  redirect
from typing import Any
from django.contrib import messages
from django.views.generic import CreateView, ListView,  TemplateView
from .models import CuotaMensual, CuotaActividad
from .forms import CuotaMensualForm, CuotaActividadForm
from django.urls import reverse_lazy, reverse
from Socios.models import Socio
from django.shortcuts import render, HttpResponseRedirect
from .forms import YearFilterForm, YearFilterForm2
from Administracion.views import ErrorView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# index buscador con lista de socios
class BuscarSocio(ListView):
    model = Socio
    template_name = 'cuotas/index_cuotas.html'
    context_object_name = 'socios'

   
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Socio.objects.filter(nroSocio__icontains=query) | Socio.objects.filter(apellido__icontains=query) | Socio.objects.filter(nombre__icontains=query)
        return Socio.objects.all()
    



# class PagoCuotaCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
#     model = CuotaMensual
#     form_class = CuotaMensualForm
#     template_name = 'cuotas/cuota_form.html'
#     success_url= reverse_lazy("index_cuotas")

#     def test_func(self):       
#         return self.request.user.groups.filter(name='Administrativo').exists()
    
#     def handle_no_permission(self):
#         return redirect('error_permiso')
    
#     def get_initial(self):
#       #  Obtiene el ID del socio desde la URL (debes configurar la URL en consecuencia)
#         socio_id = self.kwargs.get('socio_id')
#         return {'socio': socio_id}


#     def form_valid(self, form):

#         socio = form.cleaned_data['socio']
#         mes = form.cleaned_data['mes']
#         ano = form.cleaned_data['ano']

#         cuota_existente = CuotaMensual.objects.filter(socio=socio, mes=mes, ano=ano, mes_pagado=True).exists()

#         if cuota_existente:
#             messages.error(self.request, 'Esta cuota ya está registrada para este mes y año.')
#             return HttpResponseRedirect(reverse('pago_cuota'))  # Redirige nuevamente al formulario

#         response = super().form_valid(form)
#         messages.success(self.request, 'NO cuota se ha registrado correctamente.')
#         return response

    

class PagoCuotaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CuotaMensual
    form_class = CuotaMensualForm
    template_name = 'cuotas/cuota_form.html'
    success_url = reverse_lazy("index_cuotas")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    
    def get_initial(self):
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}

    def form_valid(self, form):
        socio = form.cleaned_data['socio']
        mes = form.cleaned_data['mes']
        ano = form.cleaned_data['ano']

        cuota_existente = CuotaMensual.objects.filter(socio=socio, mes=mes, ano=ano, mes_pagado=True).exists()

        if cuota_existente:
            messages.error(self.request, 'Esta cuota social ya está registrada para este mes y año.')
            return self.form_invalid(form)  # Redirige al formulario con mensajes de error

        messages.success(self.request, 'La cuota social se ha registrado correctamente.')
        return super().form_valid(form)
class CuotasAnualesListView(ListView):
    model = CuotaMensual  # Especifica el modelo a utilizar
    template_name = 'cuotas/cuotas_anuales.html'
    context_object_name = 'cuotas'  # Nombre del objeto en el contexto

    

    def get_queryset(self):
        # Obtén el ID del socio desde los parámetros de la URL
        socio_id = self.kwargs.get('socio_id')
        # Filtra las cuotas para el socio y el año seleccionado en el formulario
        ano = self.request.GET.get('ano')
        queryset = CuotaMensual.objects.filter(socio__id=socio_id, ano=ano)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = YearFilterForm()
        # Obtén el ID del socio desde los parámetros de la URL
        context['socio_id'] = self.kwargs.get('socio_id')
        return context



#                          CUOTAS DE ACTIVIDADES
#                        Regitro cuota Actividad
class PagoCuotaActCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = CuotaActividad
    form_class = CuotaActividadForm
    template_name = 'cuotas/cuota_actividad.html'
    success_url = reverse_lazy("index_cuotas")

    def test_func(self):       
        return self.request.user.groups.filter(name='Administrativo').exists()
    
    def handle_no_permission(self):
        return redirect('error_permiso')
    

    def get_initial(self):        
        socio_id = self.kwargs.get('socio_id')
        return {'socio': socio_id}
    
   
    def form_valid(self, form):
        socio = form.cleaned_data['socio']
        actividad = form.cleaned_data['actividad']
        mes = form.cleaned_data['mes']
        ano = form.cleaned_data['ano']

        cuota_existente = CuotaActividad.objects.filter(socio=socio, actividad=actividad, mes=mes, ano=ano).exists()

        if cuota_existente:
            messages.error(self.request, 'Esta cuota de actividad ya está registrada para este mes y año.')
            return self.form_invalid(form)  # Redirige al formulario con mensajes de error

        messages.success(self.request, 'La cuota de actividad se ha registrado correctamente.')
        return super().form_valid(form)
    
class ReporteCuotasAct(ListView):
    model = CuotaActividad  # Especifica el modelo a utilizar
    template_name = 'cuotas/reporte_cuotas_act.html'
    context_object_name = 'cuotas'  # Nombre del objeto en el contexto

    

    def get_queryset(self):
        # Obtén el ID del socio desde los parámetros de la URL
        socio_id = self.kwargs.get('socio_id')
        # Filtra las cuotas para el socio y el año seleccionado en el formulario
        ano = self.request.GET.get('ano')
        queryset = CuotaActividad.objects.filter(socio__id=socio_id, ano=ano)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = YearFilterForm2()
        # Obtén el ID del socio desde los parámetros de la URL
        context['socio_id'] = self.kwargs.get('socio_id')
        return context