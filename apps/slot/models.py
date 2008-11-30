from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from section.models import Section
from issue.models import Issue

from core.models import Item

class FilteredItemsManager(models.Manager):
    def get_query_set(self, issue, section):
        return super(models.Manager, self).get_query_set().filter(issue=issue, section=section).[0:self.n_items]

class Slot(models.Model):
    """
    A slot which items can be stored in.
    If there are more than n items in any particular issue/section
    then they will not appear in the manager.
    """

    items = models.ManyToManyField(Items, through='SlotItems')

    name = models.SlugField(unique=True)
    verbose_name = models.CharField(max_length=255)
    n_items = models.IntegerField()

    get_items = FilteredItemsManager()

    def __unicode__(self):
        return u"Slot '%s'" % (self.verbose_name,)

class SlotItems(models.Model):
    """
    The join table between slots and items
    """

    slot = models.ForeignKey(Slot)
    item = models.ForeignKey(Item)
    order = models.IntegerField()


