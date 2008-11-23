from section.models import *
from story.models import Story
from slot.views import generate_slot_dict
from slot.views import Slot
from section.utils import get_section_from_string
from issue.models import Issue
from django.shortcuts import render_to_response
from django.http import Http404

DEFAULT_RECENT_STORIES_LENGTH = 10

def main_page(request, sections=None, year=None, term=None, week=None):

    section = get_section_from_string(sections.split('/'))

    #For the future...
    #if year: qs.oxdate_filter(year, term, week)
    i = Issue.objects.get_current()

    context_dict = ({'section': section})
    context_dict.update(generate_slot_dict(Slot.objects.filter(section=section, issue=i)))
    #for subsection in section.children:
    #    context_dict.update(generate_slot_dict(Slot.objects.filter(section=subsection)))

    c = getattr(SectionContexts, section.slug)(section, i)
    if c:
        context_dict.update(c)
    recent_stories_qs = Story.published.unslotted(issue=i)
    recent_stories = recent_stories_qs.filter(section=section).order_by('-online_date')
    context_dict.update(
            {'recent_stories': recent_stories[:DEFAULT_RECENT_STORIES_LENGTH]})
    
    return render_to_response('section/' + section.slug + '.html', context_dict)

class SectionContexts:

    @classmethod
    def news(self, section=None, issue=None):
        nibs = Section.objects.get(slug="news-in-brief")
        nibs_qs = Story.published.filter(section=nibs)
        if issue:
            nibs_qs.filter(issue=issue)
        else:
            nibs_qs.order_by('online_date')[:9]
        return {'nibs': nibs_qs }

    @classmethod
    def debate(self, section=None, issue=None):
        pass

    @classmethod
    def features(self, section=None, issue=None):
        pass

    @classmethod
    def arts(self, section=None, issue=None):
        d = {}
        if not section:
            section = Section.objects.get(slug="arts")
        for subsection in section.children.all():
            d.update(
                    generate_slot_dict(
                        Slot.objects.filter(section=subsection, issue=issue),
                        prefix=subsection.slug+'_'))
        return d

    @classmethod
    def music(self, section=None, issue=None):
        pass

    @classmethod
    def drama(self, section=None, issue=None):
        pass

    @classmethod
    def film(self, section=None, issue=None):
        pass

    @classmethod
    def culture(self, section=None, issue=None):
        pass

    @classmethod
    def fashion(self, section=None, issue=None):
        pass

    @classmethod
    def sport(self, section=None, issue=None):
        pass

    @classmethod
    def editorials(self, section=None, issue=None):
        pass

    @classmethod
    def letters(self, section=None, issue=None):
        pass

def slot_context_wrapper(section):
    context_dict = generate_slot_dict(Slot.objects.filter(section=section))
    context_dict.update({'section': section})
    return context_dict
