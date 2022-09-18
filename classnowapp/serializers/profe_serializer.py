from rest_framework import serializers
from classnowapp.models import Profesores

class Prof_serializer(serializers.ModelSerializer):

    class Meta:
        model = Profesores
        fields = '__all__' #['id_profesores', 'username', 'nombres', 'apellidos', 'email', 'celular', 'edad', 'ciudad', 'genero', 'password', 'rol_usuario']

    def create(self, validated_data):
        userInstance = Profesores.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = Profesores.objects.get(id=obj.id)
        return {
            'id_profesores': user.id,
            'username': user.username,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'email': user.email,
            'celular': user.celular,
            'edad': user.edad,
            'ciudad': user.ciudad,
            'genero': user.genero,
            'rol_usuario': user.rol_usuario,
        }