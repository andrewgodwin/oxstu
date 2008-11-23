from django.contrib import admin
from issue.models import *

class IssueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Issue, IssueAdmin)


