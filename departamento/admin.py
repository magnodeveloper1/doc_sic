from django.contrib import admin
from .models import Departamento, DocumentoDoDepartamento

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create_at', 'updated_at', 'status')

class PastaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(DocumentoDoDepartamento, PastaAdmin)
