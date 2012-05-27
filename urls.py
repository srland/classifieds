from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('news.urls')),
    # admin interface url
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
    