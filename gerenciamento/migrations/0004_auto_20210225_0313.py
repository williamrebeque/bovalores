# Generated by Django 3.1.5 on 2021-02-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_auto_20210225_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='lim_inf',
            field=models.FloatField(verbose_name='Limite Inferior'),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='lim_sup',
            field=models.FloatField(verbose_name='Limite Superior'),
        ),
    ]