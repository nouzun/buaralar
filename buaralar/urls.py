from django.conf.urls import patterns, include, url
from django.contrib import admin
from buaralar import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buaralar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
