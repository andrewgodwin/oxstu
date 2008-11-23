from django.contrib import admin
from printissue.models import *

class IssuePrintEditionAdmin(admin.ModelAdmin):
    list_display = ("id", "issue", "section")

admin.site.register(IssuePrintEdition, IssuePrintEditionAdmin)
