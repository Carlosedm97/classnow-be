from rest_framework import serializers
from classnowapp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'nombres', 'apellidos', 'email', 'celular', 'edad', 'ciudad', 'genero', 'password', 'roles']

    """def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'email': user.email,
            'celular': user.celular,
            'edad': user.edad,
            'ciudad': user.ciudad,
            'genero': user.genero,
            'roles': user.roles,
        }""" 