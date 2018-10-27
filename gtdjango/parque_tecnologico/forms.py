from django import forms

from .models import Recurso


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'tipo_recurso']
        widgets = {
            'nombre': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_recurso': forms.Select(attrs={'class': 'form-control'})
        }