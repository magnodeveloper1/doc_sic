from django.contrib import admin
from django.utils.html import format_html
from .models import Documento, DocPartilhado, DOCUMENT_STATUS
from datetime import datetime

class PartilhadosComigo(admin.ModelAdmin):

    # display list
    list_display = ('documento', 'partilhado_por', 'partilhado_aos')
    #list_filter = ("nome", "status")
    list_per_page = 25

    def partilhado_aos(self, obj):
        return obj.create_at

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False
    
    class Meta:
        verbose_name_plural = "Partilhados Comigo"

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):

    # forms custom
    change_form_template = 'doc_form.html'
    readonly_fields = [ "status", "status_at", "utilizador", "o_documento"]

    def o_documento(self, obj):
        if obj:
            return format_html('<iframe src="/{}" style="width: 100%;height: 700px;border: none;"></iframe>', obj.documento)
        else:
            return ""

    # display list
    list_display = ('nome', 'created_at', 'status', 'validar', 'enviar')
    list_filter = ("nome", "status")
    list_per_page = 25

    # actions to dashboard
    actions = ["enviar_para_direcao"]
    def enviar_para_direcao(self, request, queryset):
        queryset.update(status=DOCUMENT_STATUS[1][0], status_at = datetime.now())

    def save_model(self, request, obj, form, change):
        obj.utilizador = request.user
        return super().save_model(request, obj, form, change)

    def response_change(self, request, obj):
        if "_send_to_aprove" in request.POST:
            obj.status = DOCUMENT_STATUS[1]
            obj.save()
            # self.message_user(request, "Enviado para aprovacao")
        elif "_share_" in request.POST:
            docpartilhado = DocPartilhado()
            docpartilhado.documento = obj
            docpartilhado.partilhado_por = request.user
            docpartilhado.partilhado_com = request.user
            docpartilhado.save()
            # self.message_user(request, "Partilhado com Sucesso!")
        
        return super().response_change(request, obj)

    def enviar(self, obj):
        return format_html('<a class="button" href="{}"><button class="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded"><i class="fas fa-message"></i></button></a>', "url")

    def validar(self, obj):
        return format_html('<a class="button" href="{}"><button class="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded"><i class="fas fa-check"></i></button></a>', "url")
    
    def has_delete_permission(self, request, obj = ...):
        return False
    
    class Meta:
        verbose_name_plural = "Meus Documentos"

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(DocPartilhado, PartilhadosComigo)