from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome da empresa')

    def __str__(self):
        return self.nome
