from rest_framework import serializers
from classnowapp.models import Account_est, User_est
from .account_est_serializer import Account_est_serializer

class User_est_serializer(serializers.ModelSerializer):
    account = Account_est_serializer()

    class Meta:
        model = User_est
        fields = ['id', 'username_est', 'nombres', 'apellidos', 'email', 'celular', 'edad', 'ciudad', 'genero', 'password', 'rol_usuario']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User_est.objects.create(**validated_data)
        Account_est.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User_est.objects.get(id=obj.id)
        account = Account_est.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username_est': user.username_est,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'email': user.email,
            'celular': user.celular,
            'edad': user.edad,
            'ciudad': user.ciudad,
            'genero': user.genero,
            'rol_usuario': user.rol_usuario,
            'account':{
                'isActive': account.isActive
            }
        }

#Carlos Lopez
