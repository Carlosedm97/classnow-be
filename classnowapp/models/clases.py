from django.db import models
from .user import User

class Clases(models.Model):
    id = models.AutoField(primary_key=True)
    tema = models.CharField('Tema', max_length=100)
    hora = models.TimeField('Hora')
    fecha = models.DateField('Fecha')
    profesor = models.ForeignKey(User, related_name="profesor", on_delete=models.CASCADE)
    estudiante = models.ForeignKey(User, related_name="estudiante", on_delete=models.CASCADE)