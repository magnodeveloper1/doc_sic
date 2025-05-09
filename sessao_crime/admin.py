from django.contrib import admin
from .models import Crime, FicheiroCrime

# Register your models here.
class CrimeAdmin(admin.ModelAdmin):
    pass

class FicheiroCrimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Crime, CrimeAdmin)
admin.site.register(FicheiroCrime, FicheiroCrimeAdmin)