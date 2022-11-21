from django.db import models
from ..departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        # ordering = ['-name']
        # unique_together = ('name','short_name')
    def __str__(self):
        return str(self.id) + '-'+self.habilidad



class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=120,blank=True)
    full_name = models.CharField('Nombres Completos',max_length=70)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleados', blank=True, null=True)
    #relacion de muchos a muchpos
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self):
        return str(self.id) + '-'+self.first_name + '-' + self.last_name


