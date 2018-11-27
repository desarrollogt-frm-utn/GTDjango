from django.shortcuts import HttpResponse, redirect, get_object_or_404

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView

from .forms import FilterRecurso, RecursoForm, TipoRecursoForm
from .models import Recurso, TipoRecurso

def index(request):
    return render(request, "base.html", )


def saludo(request, nombre):
    request.user
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


def detalle_recurso(request, id):
    recurso = get_object_or_404(Recurso, pk=id)

    return render(request, "recurso/detalle.html", {'recurso': recurso})


def eliminar_recurso(request, id):
    recurso = get_object_or_404(Recurso, pk=id)

    if request.method == "POST":
        recurso.delete()
        return redirect(reverse_lazy('listar-recurso'))

    return render(request, "recurso/eliminar.html", {'recurso': recurso})

"""

# vista basada en funciones
def listar_recursos(request):
    recursos = Recurso.objects.all()

    return render(request, "recurso/listar.html", {'recursos': recursos})
"""

# Vista basada en clases
class RecursoListView(ListView):
    model = Recurso
    context_object_name = "recursos"
    template_name = "recurso/listar.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(RecursoListView, self).get_context_data(**kwargs)

        context['filter_form'] = FilterRecurso(self.request.GET)

        return context

    def get_queryset(self):

        tipo = self.request.GET.get('tipo', '')

        try:
            if int(tipo):
                qs = Recurso.objects.filter(tipo_recurso=tipo)
            else:
                qs = Recurso.objects.all()
        except:
            qs = Recurso.objects.all()
        return qs



class RecursoUpdateView(UpdateView):
    model = Recurso
    # fields = ['nombre']
    pk_url_kwarg = 'id'
    template_name = "recurso/crear.html"
    form_class = RecursoForm

    def get_success_url(self):
        return reverse_lazy('detalle-recurso', kwargs={'id': self.object.id})

class TipoRecursoCreateView(CreateView):
    model = TipoRecurso
    template_name = "tipo_recurso/crear.html"
    form_class = TipoRecursoForm
    success_url = reverse_lazy('listar-recurso')