from django.contrib import admin
from story.models import *
from photos.models import Pool
from django.contrib.contenttypes import generic
from slot.admin import SlottedObjectInline

class PhotoPoolInline(generic.GenericTabularInline):
    model = Pool
    max_num = 1

class StoryAdmin(admin.ModelAdmin):
    list_display = ("id", "headline", "issue", "section",)
    list_display_links = ("id", "headline")
    search_fields = ("headline",)
    prepopulated_fields = {"slug": ("headline",)}
    exclude = ('updated_at',)
    list_filter = ('section',)
    filter_horizontal = ('writers', 'related_to')

    inlines = [
            PhotoPoolInline,
            SlottedObjectInline,
            ]



admin.site.register(Story, StoryAdmin)

