from django.conf.urls import patterns, url

from posts import views
from posts.views import posts_views_get_selected_day, posts_views_get_selected_event, \
    posts_views_get_selected_event_ajax

urlpatterns = patterns('',
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /posts/5/
    #url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<post_id>\d+)/$', posts_views_get_selected_event),
    url(r'^event_wAjax/(?P<post_id>\d+)$', posts_views_get_selected_event_ajax),
    url(r'^(?P<day>(today|tomorrow|nextday))/$', posts_views_get_selected_day),
)
