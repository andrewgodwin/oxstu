from django.db import models
import mptt

class Section(models.Model):  
    """
    A section contains related content, and can optionally
    be nested inside another section.
    If a section is top-level, its parent is None, else it's
    sections all the way down...
    """
        
    parent  = models.ForeignKey("self", null=True, related_name='children')
    title   = models.CharField(max_length=255)
    slug    = models.SlugField()
    order   = models.IntegerField(default=0)
    
    def get_section(sections_list):
        """
        This function takes a list of sections and returns the child node (last in list).
        Raises a 404 if the list is not a valid tree.
        """
        node = sections_list[0]
        for section in sections_list[1:]:
            if section.parent != node:
                raise Http404("Cannot find section '%s'" % section)
            else:
                node = section
        return node

    def parent_object_list(self):
        return self.get_ancestors()

    def partname(self):
        if not self.parent:
            return self.title
        else:
            return self.parent.partname() + " > " + self.title
    
    def __unicode__(self):
        return u"Section '%s'" % (self.partname())
    
    class Meta:
        unique_together = (("parent", "title"),)
    
    class Admin:
        list_display=('id','title','order')
        ordering=["order"]

mptt.register(Section, order_insertion_by=['order'])

