from django.contrib import admin
from django.urls import path
from . import views

app_name="departamento_app"

urlpatterns = [
    path('new-dep/',
         views.NewDepartamentoView.as_view(),
         name='nuevo_dep'),
    path('listadep/',
         views.DepListView.as_view(),
         name='listadep'),
    path('success_dep/',
         views.NewDepSucView.as_view(),
         name='success_dep'),
]

print(urlpatterns)