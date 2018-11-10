from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index-parque-tecnologico'),

    path('saludo/<slug:nombre>', views.saludo, name='saludo'),

    path('multiplicar/<int:a>/<int:b>', views.multiplicar, name='multiplicar'),

    path('recursos/crear', views.crear_recurso, name='crear-recurso'),

    path('recursos', views.RecursoListView.as_view(), name='listar-recurso'),

    path('recursos/<int:id>', views.detalle_recurso, name='detalle-recurso'),

    path('recursos/eliminar/<int:id>', views.eliminar_recurso, name='eliminar-recurso'),

    path('recursos/modificar/<int:id>', views.RecursoUpdateView.as_view(), name='modificar-recurso'),


    path('recursos/tipo/crear', views.TipoRecursoCreateView.as_view(), name='crear-tipo-recurso')

]
