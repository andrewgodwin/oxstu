from django.contrib import admin
from story.models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'issue', 'section')
    search_fields = ('headline',)
    prepopulated_fields = {'slug': ('headline',)}
    exclude = ('updated_at', 'views', 'created')
    list_filter = ('section',)
    filter_horizontal = ('writers', 'related_to')

admin.site.register(Story, StoryAdmin)

