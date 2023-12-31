from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    documento_funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('funcionario_update', args=[self.documento_funcionario.id])

    def __str__(self):
        return self.descricao

