from django.contrib import admin
from slot.models import Slot

class SlotAdmin(admin.ModelAdmin):
    list_display = (name, 'verbose_name')

admin.site.register(Slot, SlotAdmin)
