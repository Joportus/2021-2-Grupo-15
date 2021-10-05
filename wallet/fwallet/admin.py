from django.contrib import admin

# Register your models here.
from fwallet.models import User, RegistroDinero
 
admin.site.register(RegistroDinero)
admin.site.register(User)