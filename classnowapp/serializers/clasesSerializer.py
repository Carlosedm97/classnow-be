from rest_framework import serializers
from classnowapp.models import Clases

class ClasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clases
        fields = ['id', 'tema', 'hora', 'fecha', 'profesor', 'estudiante']