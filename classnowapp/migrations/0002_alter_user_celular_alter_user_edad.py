# Generated by Django 4.1.1 on 2022-09-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classnowapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='celular',
            field=models.CharField(max_length=15, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='user',
            name='edad',
            field=models.IntegerField(verbose_name='Edad'),
        ),
    ]
