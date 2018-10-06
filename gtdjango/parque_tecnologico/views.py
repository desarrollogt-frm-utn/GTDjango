from django.shortcuts import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("Hola Mundo")


def saludo(request, nombre):
    return HttpResponse("Hola {0!s} desde app".format(nombre))

def multiplicar(request, a, b):
    return HttpResponse("El valor de la cuenta es {0!s}".format(a * b))
