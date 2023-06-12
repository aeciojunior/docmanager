from datetime import datetime, timedelta

from django.db import models

from funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=150)
    proprietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='gestao_documentos/documento/', null=False, blank=False,
                               verbose_name='documento_anexo', help_text='Anexe um arquivo referente documento')
    data_inclusao = models.DateTimeField(help_text='Data da inclusão do documento', verbose_name='documento_data_inclusao_documento',
                                         null=False, default=datetime.now())
    link = models.CharField(max_length=150, null=True,
                            blank=True, help_text='Link de vídeo tutorial')

    def __str__(self):
        return self.descricao
