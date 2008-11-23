from slot.models import *

def generate_slot_dict(slot_list=None, prefix=''):
    """
    Takes a list of slots and returns a dict keyed by the slot name,
    attached to associated content. If list is none, return empty dict.
    """
    if slot_list: return dict([(prefix + s.name, s.content) for s in slot_list])
    else: return {}
