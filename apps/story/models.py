from django.db import models

from django.contrib.auth.models import User

from core.models import Item
from photologue.models import Photo

class Story(Item):
    """
    A simple story model
    """

    headline        = models.CharField(max_length=255)
    synopsis        = models.TextField()
    text            = models.TextField()

    slug            = models.SlugField()

    writers         = models.ManyToManyField(User, related_name="stories")

    photos          = models.ForeignKey(Photo)

    def __unicode__(self):
        return u"Story #%s '%s'" % (self.id, self.headline)

