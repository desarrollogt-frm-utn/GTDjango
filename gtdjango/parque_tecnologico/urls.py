from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index-parque-tecnologico'),

    path('saludo/<slug:nombre>', views.saludo, name='saludo'),

    path('multiplicar/<int:a>/<int:b>', views.multiplicar, name='multiplicar')

]
