from django import forms
from .models import Parroquia, BarrioCiudadela

class ParroquiaForm(forms.ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']

class BarrioCiudadelaForm(forms.ModelForm):
    class Meta:
        model = BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia']