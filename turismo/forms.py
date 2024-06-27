from django import forms
from .models import Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['precio', 'descripcion', 'imagen']