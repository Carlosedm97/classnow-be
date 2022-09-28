from django.contrib import admin
from .models import User
from .models import Clases
from .models import Account

admin.site.register(User)
admin.site.register(Clases)
admin.site.register(Account)