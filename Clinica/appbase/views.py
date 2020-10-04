from django.shortcuts import render, redirect
from django.db import models 
from django.http.response import HttpResponseForbidden 
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Horario, Agenda, Doctor, SignoVital
from .forms import PacienteForm, HorarioForm, AgendaForm, DoctorForm, SignoVitalForm

# Vista de Inicio


class InicioView(TemplateView):
    template_name = "index.html"

class PacienteView(ListView):
    model = Paciente
    template_name = "base/paciente/paciente.html"
    context_object_name = "pacientes"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context

class CrearPacienteView(CreateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"

class EditarPacienteView(UpdateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"

class EliminarPacienteView(DeleteView):
    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            paciente = Paciente.objects.get(id=pk)
            paciente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:paciente')
        except:
            return HttpResponseForbidden("NO ES POSIBLE ELIMINAR ESTE DATO, POR FAVOR REGRESE" ) 

class ListadoHorarioView(ListView):
    model = Horario
    template_name = 'base/horario/listar_horario.html'
    context_object_name = 'Horarios'

class CrearHorarioView(CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'base/horario/crear_horario.html'
    success_url = reverse_lazy('base:listar_horario')

class EditarHorarioView(UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'base/horario/crear_horario.html'
    success_url = reverse_lazy('base:listar_horario')

class EliminarHorarioView(DeleteView):
    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            agenda = Horario.objects.get(id=pk)
            agenda.delete()
            # object.estado = False
            # object.save()
            return redirect('base:listar_horario')
        except:
            return HttpResponseForbidden("NO ES POSIBLE ELIMINAR ESTE DATO, POR FAVOR REGRESE" ) 

class ListadoAgendaView(ListView):
    model = Agenda
    template_name = 'base/agenda/listar_agenda.html'
    context_object_name = 'Agendas'

class CrearAgendaView(CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'base/agenda/crear_agenda.html'
    success_url = reverse_lazy('base:listar_agenda')

class EditarAgendaView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'base/agenda/crear_agenda.html'
    success_url = reverse_lazy('base:listar_agenda')

class EliminarAgendaView(DeleteView):
    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            paciente = Agenda.objects.get(id=pk)
            paciente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:listar_agenda')
        except:
            return HttpResponseForbidden("NO ES POSIBLE ELIMINAR ESTE DATO, POR FAVOR REGRESE") 

class DoctorView(ListView):
    model = Doctor
    template_name = "base/doctores/listar_doctor.html"
    context_object_name = "doctores"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de doctores"
        return context

class CrearDoctoresView(CreateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctores/crear_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:listar_doctores')
    context_object_name = "doctores"

class EditarDoctoresView(UpdateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctores/crear_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:listar_doctores')
    context_object_name = "doctores"

class EliminarDoctoresView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            doctor = Doctor.objects.get(id=pk)
            doctor.delete()
            # object.estado = False
            # object.save()
            return redirect('base:listar_doctores')
        except:
            return HttpResponseForbidden("NO ES POSIBLE ELIMINAR ESTE DATO, POR FAVOR REGRESE") 

class SignoVitalView(ListView):
    model = SignoVital
    template_name = "base/signovital/listar_signovital.html"
    context_object_name = "signos"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 3

    def get_queryset(self):
        descripcion = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        return self.model.objects.filter(descripcion__icontains=descripcion)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descripcion'] = self.request.GET.get(
            'descripcion') if self.request.GET.get('descripcion') else ''
        context['titulo'] = "Consulta de Signos Vitales"
        return context

class CrearSignoVitalView(CreateView):
    model = SignoVital
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signovital/crear_signovital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:listar_signovital')
    context_object_name = "signos"

class EditarSignoVitalView(UpdateView):
    model = SignoVital
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signovital/crear_signovital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:listar_signovital')
    context_object_name = "signos"

class EliminarSignoVitalView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            signo = SignoVital.objects.get(id=pk)
            signo.delete()
            # object.estado = False
            # object.save()
            return redirect('base:listar_signovital')
        except:
            return HttpResponseForbidden("NO ES POSIBLE ELIMINAR ESTE DATO, POR FAVOR REGRESE" ) 