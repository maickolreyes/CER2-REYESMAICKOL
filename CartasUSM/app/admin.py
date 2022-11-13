import imp
from django.contrib import admin
from .models import Residencias, Correspondencia

# Register your models here.
admin.site.register(Residencias)
admin.site.register(Correspondencia)