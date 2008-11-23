from django.db import models

from issue.models import Issue
from section.models import Section

class IssuePrintEdition(models.Model):
    """ A downloadable (e.g. PDF of) an issue.  """
    
    issue   = models.ForeignKey(Issue)
    section = models.ForeignKey(Section, null=True)
    file    = models.FileField(upload_to="pdfs")
    
    def __unicode__(self):
        return u"IssuePrintEdition of Issue '%s', section '%s'" % (self.issue, self.section)

