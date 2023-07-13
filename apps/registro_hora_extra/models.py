from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    id = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=100)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('hora_extra_update', args=[self.id])

    def __str__(self):
        return self.motivo
