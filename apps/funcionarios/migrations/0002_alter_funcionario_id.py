# Generated by Django 3.2 on 2023-07-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
