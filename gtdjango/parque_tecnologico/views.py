from django.shortcuts import HttpResponse, redirect, get_object_or_404

from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import RecursoForm
from .models import Recurso

def index(request):
    return render(request, "base.html", )


def saludo(request, nombre):
    return render(request, "saludo.html", {'nombre': nombre})

def multiplicar(request, a, b):
    return HttpResponse("El valor de la cuenta es {0!s}".format(a * b))


def crear_recurso(request):
    form = RecursoForm()

    if request.method == "POST":
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('listar-recurso'))

    return render(request, "recurso/crear.html", {'form': form})


def listar_recursos(request):
    recursos = Recurso.objects.all()

    return render(request, "recurso/listar.html", {'recursos': recursos})


def detalle_recurso(request, id):
    recurso = get_object_or_404(Recurso, pk=id)

    return render(request, "recurso/detalle.html", {'recurso': recurso})


def eliminar_recurso(request, id):
    recurso = get_object_or_404(Recurso, pk=id)

    if request.method == "POST":
        recurso.delete()
        return redirect(reverse_lazy('listar-recurso'))

    return render(request, "recurso/eliminar.html", {'recurso': recurso})