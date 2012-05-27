from django.conf.urls.defaults import *

urlpatterns = patterns('classifieds.contact.views',
  (r'^$', 'contact_us'),
  (r'^ad/([0-9]+)/$', 'contact_ad'),
)
