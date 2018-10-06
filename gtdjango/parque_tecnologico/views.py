from django.shortcuts import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, "base.html", )


def saludo(request, nombre):
    return render(request, "saludo.html", {'nombre': nombre})

def multiplicar(request, a, b):
    return HttpResponse("El valor de la cuenta es {0!s}".format(a * b))
