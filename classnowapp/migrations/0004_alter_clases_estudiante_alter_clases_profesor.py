# Generated by Django 4.1.1 on 2022-09-22 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classnowapp', '0003_clases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clases',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clases',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to=settings.AUTH_USER_MODEL),
        ),
    ]