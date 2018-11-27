from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import RegistroForm


class UsuarioCreateView(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('listar-recurso')
