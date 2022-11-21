from django.contrib import admin
from django.urls import path
from . import views

app_name ="empleado_app"

urlpatterns = [
    path('',
         views.StartView.as_view(),
         name='inicio'),

    path('listar-todos-empleados/',
         views.ListallEmpleados.as_view(),
         name='empleados-all'),

    path('listar-by-area/<nname>',
         views.ListbyArea.as_view(),
         name='empleados_area'),

    path('listar-empleados-admin',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'),

    path('buscar-empleado', views.ListbyKeyword.as_view()),

    path('lista-de-habilidades', views.ListHabEmp.as_view()),

    path('ver-empleado/<pk>/',
         views.EmpDetView.as_view(),
         name='empleado_detail'),

    path('add-empleado/',
         views.EmpCreateView.as_view(),
        name='empleado_add'),

    path('success/',
         views.SuccessView.as_view(),
         name='correcto'),

    path('update-empleado/<pk>/',
         views.EmpUpdView.as_view(),
         name='modificar_empleado'),

    path('deleted/',
         views.DeleteSuccessView.as_view(),
         name='deleted'),
    path('delete-empleado/<pk>',
         views.EmpDelView.as_view(),
         name='eliminar-empleado'),

     ]
