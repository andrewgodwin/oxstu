from django.db import models
#import mptt

class Section(models.Model):  
    """
    A section contains related content, and can optionally
    be nested inside another section.
    If a section is top-level, its parent is None, else it's
    sections all the way down...
    """
        
    parent  = models.ForeignKey('self', null=True, related_name='children')
    title   = models.CharField(max_length=255, unique=True)
    slug    = models.SlugField(unique=True)
    order   = models.IntegerField(default=0)
    
    @property
    def partname(self):
        if not self.parent:
            return self.title
        else:
            return self.parent.partname() + " > " + self.title
    
    @classmethod
    def get_roots():
        return Section.objects.filter(parent=None)

    def __unicode__(self):
        return u"Section '%s'" % (self.partname)
    
    class Meta:
        unique_together = (('parent', 'title'),)
        ordering = ('order',)

#mptt.register(Section, order_insertion_by=['order'])

