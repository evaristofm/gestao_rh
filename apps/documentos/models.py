from django.db import models

from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    documento_funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

