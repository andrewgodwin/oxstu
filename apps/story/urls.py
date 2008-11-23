from django.conf.urls.defaults import *

from story.models import *

story_info_dict = {
        'queryset': Story.published.all(),
        'template_name': 'story.html',
        'template_object_name': 'story',
        }

urlpatterns = patterns('',
    url(r'^id/(?P<object_id>[\d]+)/$', 
        'django.views.generic.list_detail.object_detail',
        story_info_dict, name='story_id'),
    #(r'^(?P<slug>[\w-]+)/$', 
        #'django.views.generic.list_detail.object_detail',
        #story_info_dict),
    )
