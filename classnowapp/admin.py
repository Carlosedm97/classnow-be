from django.contrib import admin
from .models import User_est
from .models import Account_est
from .models import Profesores


admin.site.register(User_est)
admin.site.register(Account_est)
admin.site.register(Profesores)

# Register your models here.