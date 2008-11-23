from django.db import models
from datetime import datetime
import oxdate

from section.models import Section

class IssueManager(models.Manager):
    def get_current(self):
        return self.filter(date__lte=datetime.now())[0]
        
class Issue(models.Model):
    """ Represents an print issue.  """
    
    date    = models.DateTimeField()
    title   = models.CharField(max_length=255)
    slug    = models.SlugField()

    objects = IssueManager()

    def __unicode__(self):
        return u"Issue from %s" % oxdate.OxfordDate(self.date).strftime("Week %u, %T %Y")
    
    def main_download(self):
        return IssuePrintEdition.objects.get(issue=self, section__isnull=True)
    
    def downloads(self):
        for section in Section.objects.order_by("order"):
            try:
                yield IssuePrintEdition.objects.get(issue=self, section=section)
            except IssuePrintEdition.DoesNotExist:
                pass
    
    @property
    def oxdate(self):
        return oxdate.OxfordDate(self.date)

    class Meta:
        ordering = ('-date',)

