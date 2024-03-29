# Generated by Django 4.2 on 2023-05-02 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_documento_arquivo_documento_data_inclusao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 16, 16, 37, 917696), help_text='Data da inclusão do documento', verbose_name='documento_data_inclusao_documento'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='descricao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
