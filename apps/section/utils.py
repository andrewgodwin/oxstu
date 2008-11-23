from section.models import Section
from django.http import Http404

def get_section_from_string(sections_string_list=None, parent=None):
    print sections_string_list
    for section_string in sections_string_list:
        if section_string:
            try:
                parent = Section.objects.get(parent=parent, slug=section_string)
            except Section.DoesNotExist:
                raise Http404("Sorry, section '%s' doesn't exist." % sections_string_list)
    return parent
