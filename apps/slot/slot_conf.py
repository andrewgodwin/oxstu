from django.contrib.contenttypes.models import ContentType
from story.models import *
from photos.models import *

STORY_CONTENT_TYPE = ContentType.objects.get_for_model(Story)
PHOTO_CONTENT_TYPE = ContentType.objects.get_for_model(Story)

DEFAULT_SLOTS = [
        ('Top Story', 'top_story', 1, STORY_CONTENT_TYPE),
        ('Top Photo', 'top_photo', 1, PHOTO_CONTENT_TYPE),
        ('Top Stories', 'top_stories', 5, STORY_CONTENT_TYPE),
        ]

NEWS = DEFAULT_SLOTS
ARTS = DEFAULT_SLOTS
SPORTS = DEFAULT_SLOTS
FEATURES = DEFAULT_SLOTS
MUSIC = DEFAULT_SLOTS
DRAMA = DEFAULT_SLOTS
FILM = DEFAULT_SLOTS
CULTURE = DEFAULT_SLOTS

