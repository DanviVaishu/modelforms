from django.contrib import admin
from app.models import *
class CustomizewebPage(admin.ModelAdmin):
    list_display=['Topic_Name','name','url','Email']
    list_display_links=['name']
    list_editable=['Email']
admin.site.register(Topic)
admin.site.register(Webpage, CustomizewebPage)
admin.site.register(AccessRecord)

