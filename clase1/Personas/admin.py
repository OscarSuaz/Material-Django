from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Persona)
admin.site.register(Enfermero)
admin.site.register(Trabajo)

