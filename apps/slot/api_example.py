from django.db import models

# Create your models here.
i = Issue(date=datetime.now)
s = Section(name="Arts")
p = IssueSectionSlotPool(issue=i, section=s)

s = Story.objects.get(id=1)
f = Photo.objects.get(id=2)
sl1 = Slot(content_object=s, name="top-story", slot_pool=p)
sl2 = Slot(content_object=f, name="top-photo", slot_pool=p)


# In the template, I'd like to pass a section and an issue to get a pool

p = IssueSectionSlotPool.objects.get(issue=i, section=s)

# Then I'd like to return the related slots, ideally based on their slotname but I presume that's not really a possibility

# Ideal api
{{ p.top_story }}, {{ p.top_photo }}

#Some reasonable approximation would be enough.
