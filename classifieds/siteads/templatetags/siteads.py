"""
  $Id$
"""
from django import template
from django.utils.safestring import mark_safe

from classifieds.siteads.models import SiteAd

from django.conf import settings

import random

register = template.Library()

class SiteAdNode(template.Node):
	def __init__(self, slot_string):
		self.slot_string = slot_string
	
	def render(self, context):
		output = ''
		number = 1
		if self.slot_string == 'sponsored':
			number = int(settings.SPONSORED_ADS_COUNT)
		
		for x in range(0, number):
			try:
				ad = random.choice(SiteAd.objects.filter(slot=self.slot_string,enabled=True,site__id__exact=settings.SITE_ID))
				output += ad.html
			except IndexError:
				pass
			
		return mark_safe(output)

def do_sitead(parser, token):
	# from the django docs...
	try:
		# split_contents() knows not to split quoted strings.
		tag_name, slot_string = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
	
	if not (slot_string[0] == slot_string[-1] and slot_string[0] in ('"', "'")):
		raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
	return SiteAdNode(slot_string[1:-1])

register.tag('sitead', do_sitead)

