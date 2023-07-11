from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departamentos.models import Departamentos
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('funcionarios_list')

    def __str__(self):
        return self.nome


