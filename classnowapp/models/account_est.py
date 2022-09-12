from django.db import models
from .user_est import User_est

class Account_est(models.Model):
    id = models.AutoField(primary_key=True)
    username_est = models.ForeignKey(User_est, related_name='account', on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)