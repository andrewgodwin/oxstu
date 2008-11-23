from django.contrib import admin
from slot.models import *
from django.contrib.contenttypes import generic

class SlottedObjectInline(generic.GenericTabularInline):
    model = SlottedObject

class SlotAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', 'section', 'issue')
    filter = ('section', 'issue')

admin.site.register(Slot, SlotAdmin)
