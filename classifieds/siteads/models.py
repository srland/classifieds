"""
  $Id$
"""
from django.db import models
from django.contrib.sites.models import Site

class SiteAd(models.Model):
	SLOT_CHOICES = (
	 ('header', 'Header'),
	 ('sidebar', 'Sidebar'),
	 ('footer', 'Footer'),
	 ('sponsored', 'Search Results'),
	)
	slot = models.CharField(max_length=32, choices=SLOT_CHOICES)
	site = models.ManyToManyField(Site)
	title = models.CharField(max_length=200)
	html = models.TextField()
	enabled = models.BooleanField()
	
	def __unicode__(self):
		return self.get_slot_display() + u' ad: "' + self.title + u'"'
	

