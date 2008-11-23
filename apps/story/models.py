from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

from tagging.fields import TagField
#from tagging.models import Tag

from django.contrib.contenttypes import generic
from photos.models import Pool
from issue.models import Issue
from section.models import Section
import oxdate
from slot.models import SlottedObject
from slot.managers import SlottedObjectManager

try:
    from notification import models as notification
    from django.db.models import signals
except ImportError:
    notification = None

class PublishedStoryManager(SlottedObjectManager):
    def get_query_set(self):
        return super(PublishedStoryManager, self).get_query_set().filter(state__exact=Story.PUBLISHED)

        
class Story(models.Model):
    """ Story
    """
    DRAFT = 0
    PUBLISHED = 1
    RETRACTED = 2

    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Public')),
        (RETRACTED, _('Retracted')),
    )
    headline        = models.CharField(_('headline'), max_length=200)
    slug            = models.SlugField(_('slug'))
    writers         = models.ManyToManyField(User, related_name="stories")
    text            = models.TextField(_('text'))
    synopsis        = models.TextField(_('standfirst'))
    state           = models.IntegerField(_('state'), choices=STATUS_CHOICES, default=1)
    allow_comments  = models.BooleanField(_('allow comments'), default=True)
    online_date     = models.DateTimeField(_('date published online'), default=datetime.now)
    created         = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at      = models.DateTimeField(_('updated at'))
    tags            = TagField()
    photos          = generic.GenericRelation(Pool)
    related_to      = models.ManyToManyField("self", blank=True, null=True)
    issue           = models.ForeignKey(Issue, blank=True, null=True)
    section         = models.ForeignKey(Section)

    slots           = generic.GenericRelation(SlottedObject)
    
    objects         = models.Manager()
    published       = PublishedStoryManager()

    @property
    def display(self):
        if state == PUBLISHED:
            return True
        else:
            return False

    @property
    def date(self):
        if self.issue:
            return self.issue.date
        elif self.updated_at:
            return self.updated_at
        elif self.online_date:
            return self.online_date
        else:
            return self.created_at

    @property
    def oxdate(self):
        return oxdate.OxfordDate(self.date)

    @property
    def photo(self):
        if self.photos.all() : return self.photos.all()[0].photo

    def get_absolute_url(self):
        return '/story/id/%s' % self.id

    def __unicode__(self):
        return u"Story #%s '%s'" % (self.id, self.headline)

    class Meta:
        verbose_name        = _('story')
        verbose_name_plural = _('stories')
        ordering            = ('-online_date',)
        get_latest_by       = 'online_date'

    #@permalink
    #def get_absolute_url(self):
    #    return ('blog_post', None, {
    #        'username': self.author.username,
    #        'year': self.publish.year,
    #        'month': "%02d" % self.publish.month,
    #        'slug': self.slug
    #})

    def save(self, force_insert=False, force_update=False):
        self.updated_at = datetime.now()
        self.text = '\n\n'.join([l for l in self.text.splitlines() if l])
        super(Story, self).save(force_insert, force_update)


# handle notification of new comments
from threadedcomments.models import ThreadedComment
def new_comment(sender, instance, **kwargs):
    if isinstance(instance.content_object, Story):
        story = instance.content_object
        if notification:
            notification.send(story.writers, "story_comment",
                    {"user": instance.user, "story": story, "comment": instance})

signals.post_save.connect(new_comment, sender=ThreadedComment)
