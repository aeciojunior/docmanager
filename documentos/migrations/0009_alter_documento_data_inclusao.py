# Generated by Django 4.2 on 2023-05-04 01:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0008_alter_documento_data_inclusao_alter_documento_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='data_inclusao',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 22, 19, 9, 706106), help_text='Data da inclusão do documento', verbose_name='documento_data_inclusao_documento'),
        ),
    ]