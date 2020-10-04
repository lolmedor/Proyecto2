from django import forms
from django.db.models import fields
from .models import Paciente, Horario, Agenda, Doctor, SignoVital


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ('dia','desde','hasta','estado')
        label = {
            'dia':'Dia Semana',
            'desde':'Hora Desde',
            'hasta':'Hora Hasta',
            'estado':'Estado'
        }
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholeder': 'Dia de la Semana'
                }
            ),
            'desde': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),
            'hasta': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        label = {
            'paciente':'Pacientes',
            'fecha':'Fecha de Agenda',
            'hora':'Hora',
            'motivo':'Motivo de consulta',
            'estado':'Estado'
        }
        widgets = {
            'paciente': forms.Select(
                attrs={
                     'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),
            'motivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'duracion': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'hh:mm'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class SignoVitalForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango1': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rango2': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'media': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }