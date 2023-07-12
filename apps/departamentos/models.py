from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa


class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    @staticmethod
    def get_absolute_url():
        return reverse('departamentos_list')

    def __str__(self):
        return self.nome
