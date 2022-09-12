# Generated by Django 4.1.1 on 2022-09-11 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_est',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username_est', models.CharField(max_length=15, unique=True, verbose_name='Username_est')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=20, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('celular', models.CharField(max_length=30, verbose_name='Celular')),
                ('edad', models.CharField(max_length=10, verbose_name='Edad')),
                ('ciudad', models.CharField(max_length=20, verbose_name='Ciudad')),
                ('genero', models.CharField(max_length=5, verbose_name='Genero')),
                ('password', models.CharField(max_length=250, verbose_name='Contraseña')),
                ('rol_usuario', models.CharField(max_length=20, verbose_name='Rol Usuario')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account_est',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isActive', models.BooleanField(default=True)),
                ('username_est', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]