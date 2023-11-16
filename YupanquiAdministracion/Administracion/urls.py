from django.urls import path
from . import views


urlpatterns =[

    
    # path('', views.Index.as_view(), name='home_administracion'),
    path('profesores/', views.ProfesoresListView.as_view() , name='lista_profesores'),
    path('editar_profesor/<int:pk>', views.EditarProfesor.as_view() , name='editar_profesor'),
    path('detalle_profesor/<int:pk>',views.DetalleProfesor.as_view(),name='detalle_profesor'),
    path('crear_profesor/',views.CrearProfesor.as_view(), name='crear_profesor'),
    path('eliminar_profesor/<int:pk>', views.EliminarProfesor.as_view(), name='eliminar_profesor'),

    path('actividades/', views.ActividadesListView.as_view() , name='lista_actividades'),
    path('crear_actividad/', views.CrarActividad.as_view() , name='crear_actividad'),
    path('editar_actividad/<int:pk>', views.EditarActividad.as_view() , name='editar_actividad'),
    path('detalle_actividad/<int:pk>',views.DetalleActividad.as_view(),name='detalle_actividad'),
    path('eliminar_actividad/<int:pk>',views.EliminarActividad.as_view(),name='eliminar_actividad'),
    


    path('categorias/',views.CategoriasListView.as_view(), name='lista_categorias'),
   
    path('detalle_categoria/<int:pk>', views.DetalleCategoria.as_view(), name='detalle_categoria'),
    path('crear_categoria/',views.CrearCategoria.as_view(),name='crear_categoria'),
    path('editar_categoria/<int:pk>',views.EditarCategoria.as_view(), name="editar_categoria"),
    path('eliminar_categoria/<int:pk>',views.EliminarCategoria.as_view(),name='eliminar_categoria'),
  
    
 ]