# Generated by Django 4.2 on 2023-05-02 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('documentos', '0002_alter_documento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.funcionario'),
        ),
    ]
