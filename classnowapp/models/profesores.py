from django.db import models
from django.contrib.auth.hashers import make_password


class Profesores(models.Model):
    id_profesores = models.BigAutoField(primary_key=True)
    username = models.CharField('Username_prof', max_length=15, unique=True)
    nombres = models.CharField('Nombres', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    email = models.EmailField('Email', max_length=30)
    celular = models.CharField('Celular', max_length=30)
    edad = models.CharField('Edad', max_length=10)
    ciudad = models.CharField('Ciudad', max_length=20)
    genero = models.CharField('Genero', max_length=5)
    password = models.CharField('Contraseña', max_length=250)
    rol_usuario = models.CharField('Rol Usuario', max_length=20)


def save(self, **kwargs):
        some_salt = 'a2sp16wxv139ñlj487khc24'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)