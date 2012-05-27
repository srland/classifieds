"""
  $Id$
"""
from django.shortcuts import render_to_response
from django.contrib.sites.models import Site

def human_sitemap(request):
	current_site = Site.objects.get_current()
	flatpages = current_site.flatpage_set.all().order_by('title')
	pages = []
	for page in flatpages:
		pages.append( {'letter': page.title[0], 'page': page} )
	
	return render_to_response("sitemaps/human.html", {'pages': pages})


