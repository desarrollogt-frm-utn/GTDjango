from django import forms

from .models import Recurso, TipoRecurso


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nombre', 'tipo_recurso']
        widgets = {
            'nombre': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_recurso': forms.Select(attrs={'class': 'form-control'})
        }


class TipoRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoRecurso
        fields = ['nombre', 'indetificador']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'indetificador': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'indetificador': "Identificador"
        }


    def clean_nombre(self):
        nombre = self.data['nombre']

        if len(nombre) < 3:
            raise forms.ValidationError(
                "La longitud del campo nombre es menor a 3"
            )

        return nombre


class FilterRecurso(forms.Form):
    tipo = forms.ModelChoiceField(
        required=False,
        queryset=TipoRecurso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
