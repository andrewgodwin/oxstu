from django.contrib import admin
from printissue.models import IssuePrintEdition

class IssuePrintEditionAdmin(admin.ModelAdmin):
    list_display = ("issue", "section")

admin.site.register(IssuePrintEdition, IssuePrintEditionAdmin)
