from slot.models import Slot
from section.models import Section
from slot import slot_conf

def issue_slot_generator(issue):
    """
    Takes an issue and generates all the slots for all the sections
    in that issue, according to the configuration in slot_conf.
    """

    for section in Section.objects.all():
        try:
            slots = getattr(slot_conf, section.slug.upper())
        except AttributeError:
            slots = []
        for slot_tuple in slots:
            s, need_save = Slot.objects.get_or_create(issue=issue, section=section, name=slot_tuple[1])
            if not s.length == slot_tuple[2]:
                s.length = slot_tuple[2]
                need_save = True
            if not s.verbose_name == slot_tuple[0]:
                s.verbose_name = slot_tuple[0]
                need_save = True
            if not s.content_type == slot_tuple[3]:
                s.content_type = slot_tuple[3]
                need_save = True
            if need_save:
                s.save()


