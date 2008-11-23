from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from section.models import Section
from issue.models import Issue

class Slot(models.Model):
    """
    A Template Slot. Designed to be a name for place a content object will
    occupy in a template.

    For example: "top-story" and "top-photo".
    """
    verbose_name = models.CharField(_('verbose name'), max_length=50)
    name = models.SlugField(_('name'))
    section = models.ForeignKey(Section, null=True, blank=True)
    issue = models.ForeignKey(Issue, null=True, blank=True)
    date = models.DateTimeField(_('date'), null=True, blank=True)
    length = models.IntegerField(_('length'), default=1)
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'), null=True)

    @property
    def is_list(self):
        return self.length > 1

    @property
    def content(self):
        if self.is_list: return [o.object for o in self.content_objects.all()]
        try:
            return self.content_objects.all()[0].object
        except:
            pass

    class Meta:
        ordering = ('-date', 'issue', 'section', 'name',)
        verbose_name = _('slot')
        verbose_name_plural = _('slots')
        unique_together = ("name", "section", "issue")

    def __unicode__(self):
        s = "%s in %s from %s" % (self.verbose_name, self.section, self.issue)
        if self.is_list: return s + ' (%d/%d)' % (self.content_objects.count(), self.length)
        else: return s

    class LengthError(Exception):
        """
        This exception indicates that the data in the database does not conform to the 
        specified slot length.
        """
        pass

class SlottedObject(models.Model):
    slot = models.ForeignKey(Slot, verbose_name=_('slot'), related_name='content_objects')
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id    = models.PositiveIntegerField(_('object id'), db_index=True)
    object       = generic.GenericForeignKey('content_type', 'object_id')
    order        = models.IntegerField(_('order'), null=True, blank=True)

    def __unicode__(self):
        return "%s in %s" % (self.object, self.slot.name)

    class Meta:
        ordering = ('order',)
        verbose_name = _('slotted object')
        verbose_name_plural = _('slotted objects')
