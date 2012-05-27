"""
  $Id$
"""
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment this for admin:
#from django.contrib import admin


# Uncomment to load INSTALLED_APPS admin.py module for default AdminSite instance.
#admin.autodiscover()

urlpatterns = patterns('',
	#todo:
	(r'^$', 'iportal.classifieds.adposting.views.index'),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	# "cool" extras
	#(r'^admin/newsletter/subscribers/$', 'accounts.views.newsletter_subscribers'),
	#(r'^sitemap/$', 'sitemaps.human_sitemap'),
	
	# Uncomment this for admin:
	#(r'^admin/(.*)', admin.site.root),

	# generic and contrib views
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset'),
	
	# our views (included from the apps)
	(r'^ads/', include('iportal.classifieds.adposting.urls')),
	(r'^contact/', include('iportal.classifieds.contact.urls')),
	
	# add-on apps.
	(r'^registration/', include('registration.urls')),
	(r'^profiles/', include('profiles.urls'), {'success_url': '/profiles/edit/'}),
)

