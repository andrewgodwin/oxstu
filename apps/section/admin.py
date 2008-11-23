from django.contrib import admin
from section.models import *

class SectionAdmin(admin.ModelAdmin):
    list_display=('id','title','order')
    ordering=["order"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Section, SectionAdmin)
