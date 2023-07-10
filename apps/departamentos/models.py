from django.db import models


class Departamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome