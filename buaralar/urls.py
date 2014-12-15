from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from buaralar import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buaralar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls')),
    url(r'^about', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^ajaximage/', include('ajaximage.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
