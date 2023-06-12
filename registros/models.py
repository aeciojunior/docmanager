from django.db import models

from funcionarios.models import Funcionario

# Create your models here.


class Registros(models.Model):
    historico = models.CharField(max_length=150)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.historico
