from django.contrib import admin
from .models import Departamento, DocumentoDoDepartamento, DocumentoEnviado, APROVATION_STATUS
# from django.contrib.auth.models import User
from documento.models import Documento

class DocumentoInline(admin.StackedInline):
    model = Documento

class EnviadosAdmin(admin.ModelAdmin):
    # forms custom
    change_form_template = 'aprove_form.html'

    # inlines = [DocumentoInline]
    list_display = ('documento', 'created_at', 'user_enviou', 'estado_de_aprovacao')

    def get_list_display(self, request):

        return super().get_list_display(request)

    # change
    def response_change(self, request, obj):
        
        if '_aprove' in request.POST:
            obj.estado_de_aprovacao = APROVATION_STATUS[1][0]
        if '_rejeitar_' in request.POST:
            obj.estado_de_aprovacao = APROVATION_STATUS[2][0]

        return super().response_change(request, obj) 

    def has_delete_permission(self, request, obj = ...):
        return False

    def save_model(self, request, obj, form, change):
        obj.user_enviou = request.user
        return super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "documento":
            if 'data_doc' in request.GET:
                kwargs["queryset"] = Documento.objects.filter(nome__in=[request.GET['data_doc']])

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create_at', 'updated_at', 'status')

class PastaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(DocumentoDoDepartamento, PastaAdmin)
admin.site.register(DocumentoEnviado, EnviadosAdmin)
