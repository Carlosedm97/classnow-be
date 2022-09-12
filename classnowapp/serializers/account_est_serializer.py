from classnowapp.models.account_est import Account_est
from rest_framework import serializers

class Account_est_serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_est
        fields = ['isActive']