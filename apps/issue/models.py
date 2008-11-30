from django.db import models
from datetime import datetime
import oxdate


class CurrentIssueManager(models.Manager):
    def get_current(self):
        return super(models.Manager, self).get_query_set().filter(date__lte=datetime.now())


class Issue(models.Model):
    """
    A single issue, on which the publishing system of the
    entire site revolves.
    """
    
    date      = models.DateTimeField()

    displayed = CurrentIssueManager()

    def __unicode__(self):
        return u"Issue from '%s'" % oxdate.OxfordDate(self.date).strftime("Week %u, %T %Y")
    
    @property
    def oxdate(self):
        return oxdate.OxfordDate(self.date)

    class Meta:
        ordering = ('-date',)

