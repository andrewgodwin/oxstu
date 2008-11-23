# Create your views here.
from story.models import Story
from django.views.generic.list_detail import object_list
from section.utils import get_section_from_string

def story_list(request, qs=Story.published.all(),
        section=None, year=None, term=None, week=None, issue=None):
    if section: qs.filter(section=get_section_from_string(section.split('/')))
    if year: qs.oxdate_filter(year, term, week)
    if issue: qs.filter(issue=issue)
    return object_list(request, queryset=qs)


