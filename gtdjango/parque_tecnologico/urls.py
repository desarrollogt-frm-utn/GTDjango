from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.index), name='index-parque-tecnologico'),

    path('saludo/<slug:nombre>', views.saludo, name='saludo'),

    path('multiplicar/<int:a>/<int:b>', views.multiplicar, name='multiplicar'),

    path('recursos/crear', login_required(views.crear_recurso), name='crear-recurso'),

    path('recursos', login_required(views.RecursoListView.as_view()), name='listar-recurso'),

    path('recursos/<int:id>', login_required(views.detalle_recurso), name='detalle-recurso'),

    path('recursos/eliminar/<int:id>', login_required(views.eliminar_recurso), name='eliminar-recurso'),

    path('recursos/modificar/<int:id>', login_required(views.RecursoUpdateView.as_view()), name='modificar-recurso'),


    path('recursos/tipo/crear', login_required(views.TipoRecursoCreateView.as_view()), name='crear-tipo-recurso')

]
