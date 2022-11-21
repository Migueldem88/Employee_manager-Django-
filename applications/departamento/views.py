from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from .forms import NewDepartmentForm
from ..empleados.models import Empleado
from .models import Departamento

class DepListView(ListView):
    template_name = "departamento/lista.html"
    model=Departamento
    context_object_name = 'departamentos'


#FormView. no vinculada con un modelo directamente
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_depart.html'
    form_class = NewDepartmentForm
    success_url = '/success_dep'

    #debemos sobreescribir
    def form_valid(self, form):
        depa=Departamento(
        name=form.cleaned_data['departamento'],
        short_name=form.cleaned_data['short_name'],)
        depa.save()
        return super(NewDepartamentoView,self).form_valid(form)

class NewDepSucView(TemplateView):
    template_name = "departamento/success_dep.html"

# nombre = form.cleaned_data['nombre']
# apellido = form.cleaned_data['apellidos']
# Empleado.objects.create(
#     first_name=nombre,
#     last_name=apellido,
#     job='1',
#     departamento=depa
# )
# return super(NewDepartamentoView,self).form_valid(form)
