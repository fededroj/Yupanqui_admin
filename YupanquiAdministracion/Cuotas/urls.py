from django.urls import path
from .views import   BuscarSocio, PagoCuotaCreateView, CuotasAnualesListView, PagoCuotaActCreateView,ListaSociosActividadView, ReporteCuotasAct

urlpatterns = [

    path('', BuscarSocio.as_view(), name='index_cuotas'),  
        # cuota Social 
    path('pago_cuota/<int:socio_id>', PagoCuotaCreateView.as_view(), name='pago_cuota'),
    path('cuotas_anuales/<int:socio_id>/', CuotasAnualesListView.as_view(), name='cuotas_anuales'),
    #     cuota actividades
    path('pago_actividad/<int:socio_id>/', PagoCuotaActCreateView.as_view(), name='pago_cuota_act'),
    path('cuotas_actividad/<int:socio_id>/',ReporteCuotasAct.as_view(), name='cuotas_actividad'),

    path('lista_socios_actividad/', ListaSociosActividadView.as_view(), name='lista_socios_actividad'),

   
]