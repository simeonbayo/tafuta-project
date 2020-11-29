from django.contrib import admin
from django.contrib.admin import ModelAdmin,register
from .models import User, Document, DocUpload, DocRequest, NotFound, ServiceRequest

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','docname')

@admin.register(DocUpload)
class DocUploadAdmin(admin.ModelAdmin):
    list_display = ('doctype','docfile','docfile_two','uploaded_at','uploaded_by','district','location')

@admin.register(DocRequest)
class DocRequestAdmin(admin.ModelAdmin):
    list_display = ('doc_requester','requested_doc','requested_date','urgency','current_address','doc_request_status')

@admin.register(NotFound)
class NotFound(admin.ModelAdmin):
    list_display = ('doc_requester','doctype','requested_date','doc_lost_location','urgency','current_address')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service_requester','service_type','doctype','requested_date')


'''
admin.site.register(User)
admin.site.register(Document)
admin.site.register(DocUpload)
admin.site.register(DocRequest)
admin.site.register(NotFound)
admin.site.register(ServiceRequest)
'''