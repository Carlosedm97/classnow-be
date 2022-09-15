from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError("User must have an username.")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username = username,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User_est(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username_est = models.CharField('Username', max_length=15, unique=True)
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

    objects = UserManager()
    USERNAME_FIELD = 'username_est'