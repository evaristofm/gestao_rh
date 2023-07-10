from django.db import models


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str__(self):
        return self.nome
