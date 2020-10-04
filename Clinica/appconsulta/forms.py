from django import forms
from django.db.models import fields
from .models import Receta, DetalleReceta, TomarSignoVital

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('paciente','motivo','sintoma','exploracion','diagnostico','gabinete','instrucciones','estado')
        label = {
            'paciente':'Paciente',
            'motivo':'Motivo',
            'sintoma':'Sintoma',
            'exploracion':'Esploracion',
            'diagnostico':'Diagnostico',
            'gabinete':'Gabinete',
            'instrucciones':'Instrucciones',
            'estado':'Estado'
        }
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'motivo': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sintoma': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'exploracion': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'diagnostico': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'gabinete': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'instrucciones': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class DetalleRecetaForm(forms.ModelForm):
    class Meta:
        model = DetalleReceta
        fields = ('receta','medicamento','cantidad','dosis','frecuencia','duracion')
        label = {
            'receta':'Receta',
            'medicamento':'Medicamento',
            'cantidad':'Cantidad',
            'docisis':'Docisis',
            'frecuaencia':'Frecuaencia',
            'duracion':'Duracion',
        }
        widgets = {
            'receta': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'medicamento': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cantidad': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'dosis': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'frecuencia': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'duracion': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class TomaSignos(forms.ModelForm):
    class Meta:
        model = TomarSignoVital
        fields = ('receta','signovital','valor','estado')
        label = {
            'receta':'Receta',
            'signovital':'Signovital',
            'valor':'Valor',
            'estado':'Estado',
        }
        widgets = {
            'receta': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'signovital': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'valor': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
