from django.contrib import admin
from .models import inventario, medico, conferencia, consulta

# Register your models here.
admin.site.register(inventario)
admin.site.register(medico)
admin.site.register(conferencia)
admin.site.register(consulta)