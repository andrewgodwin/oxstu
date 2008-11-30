from django.db import models

from tagging.fields import TagField
from datetime import datetime
import oxdate

from issue.models import Issue
from section.models import Section

class DisplayedItemsManager(models.Manager):
    def get_query_set(self):
        return super(models.Manager, self).get_query_set().filter(display=true)


class Item(models.Model):
    """
    The item model from which all items inherit.
    eg. story, photoinstance, etc
    """

    DRAFT = 0
    PUBLISHED = 1
    RETRACTED = 2

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Public'),
        (RETRACTED, 'Retracted'),
    )

    issue           = models.ForeignKey(Issue)
    section         = models.ForeignKey(Section, null=True)

    tags            = TagField()

    created         = models.DateTimeField('created at', default=datetime.now())
    updated_at      = models.DateTimeField('updated at')

    views           = models.IntegerField(default=0)

    state           = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)

    allow_comments  = models.BooleanField('allow comments', default=True)

    related_to      = models.ManyToManyField('self')

    displayed       = DisplayedItemsManager()

    @property
    def display(self):
        return (state == PUBLISHED) and (self.date > datetime.now())

    @property
    def date(self):
        return issue.date

    @property
    def oxdate(self):
        return oxdate.OxfordDate(self.date)

    def __unicode__(self):
        return u"Item #%s" % (self.id,)

    class Meta:
        ordering = ('-issue__.date',)
        get_latest_by = 'issue__date'

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        super(Item, self).save(force_insert, force_update)


