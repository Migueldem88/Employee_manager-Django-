from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .models import Empleado
from .forms import EmpleadoForm

class StartView(TemplateView):
    """view that loads start page"""
    template_name = 'inicio.html'


class ListallEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword",'')
        #jorge = j
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista
class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/list_empleados.html'
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = 'empleados'
    model=Empleado


class ListbyArea(ListView):
    #lista empleados de un area
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #recoge lo que está mandando
        area = self.kwargs['nname']
        lista = Empleado.objects.filter(
        departamento__short_name__iexact=area

    )

        return lista

class ListbyKeyword(ListView):
    """Lista por palabras clave"""
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #print('wgfwefwef')
        #recebemos las solicitudes que envia el servidor mediante request
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__iexact=palabra_clave

        )
        return lista

class ListHabEmp(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpDetView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpDetView, self).get_context_data(**kwargs)
        print(context)
        context['titulo'] = 'Empleado del mes'
        return context

class EmpCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def form_valid(self,form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name+' '+empleado.last_name
        empleado.save()
        print(empleado)
        return super(EmpCreateView,self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class DeleteSuccessView(TemplateView):
    template_name = "empleados/deleted.html"

class EmpUpdView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',

    ]

    success_url = reverse_lazy('empleado_app:empleados_admin')

    #guardar antes de ser validados por form_valid
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        print('******Metodo form valid*****')
        return super(EmpUpdView,self).form_valid(form)

class EmpDelView(DeleteView):
    model = Empleado
    template_name = "empleados/deleteview.html"
    success_url = reverse_lazy('empleado_app:empleados_admin')
