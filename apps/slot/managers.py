from django.db import models
from slot.models import *
from django.contrib.contenttypes.models import ContentType

class SlottedObjectManager(models.Manager):

    def slotted(self, issue=None, slot_name=None):
        c = ContentType.objects.get_for_model(self.model)
        qs = SlottedObject.objects.filter(content_type=c)
        if issue:
            qs.filter(slot__issue=issue)
        if slot_name:
            qs.filter(slot__name=slot_name)
        return qs

    def unslotted(self, issue=None, slot_name=None):
        list = [object.id for object in self.slotted(issue, slot_name)]
        return self.exclude(id__in=list)
