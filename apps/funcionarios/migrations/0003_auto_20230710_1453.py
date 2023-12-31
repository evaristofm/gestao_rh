# Generated by Django 3.2 on 2023-07-10 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_alter_empresa_id'),
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0002_alter_funcionario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.Departamentos'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
