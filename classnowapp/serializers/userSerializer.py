from rest_framework import serializers
from classnowapp.models import User, Account
from .accountSerializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'nombres', 'apellidos', 'email', 'celular', 'password', 'rol', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'email': user.email,
            'celular': user.celular,
            'rol': user.rol,
            'account': {
                'id': account.id,
                'lastChangeDate': account.lastChangeDate, 
                'isActive': account.isActive
            }
        }