from django.contrib import admin
from section.models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display=('title', 'parent')
    ordering=['order']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Section, SectionAdmin)
