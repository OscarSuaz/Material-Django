from django.contrib import admin

from .models import *
# Register your models here.
class ComentsAdmin(admin.TabularInline):
    model=Coment
    extra=2

class PublicAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':['titulo','body']}),
        ('Info_tiempo', {'fields':['fecha_public']}),
    ]
    inlines=[ComentsAdmin]

admin.site.register(Post,PublicAdmin)
#admin.site.register(Coment)