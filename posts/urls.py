from django.conf.urls import patterns, url

from posts import views
from posts.views import get_selected_event

urlpatterns = patterns('',
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /posts/5/
    #url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>\d+)/$', get_selected_event),
)
