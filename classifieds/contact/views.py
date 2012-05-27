from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.utils.translation import ugettext as _

from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site

from django.core.mail import EmailMessage, send_mail

from classifieds.adposting.models import Ad

import datetime

from forms import ContactForm, ContactUploadForm

def contact_us(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			# send email when done
			# 1. render context to email template
			email_template = loader.get_template('contact/email/contact_us.txt')
			context = RequestContext(request, {'data': form.cleaned_data})
			email_contents = email_template.render(context)
			# 2. send email
			
			send_mail(_('User contact from ') + Site.objects.get_current().name, email_contents, settings.FROM_EMAIL, [settings.FROM_EMAIL], fail_silently=False)
			
			# create thank you message
			try:
				request.user.message_set.create(message=_("Your message has been sent."))
			except:
				pass
			
			return HttpResponseRedirect('/contact/received/')
	else:
		form = ContactForm()
		
	return render_to_response("contact/us.html", {'form': form}, context_instance=RequestContext(request))
	
def contact_ad(request, adId):
	ad = get_object_or_404(Ad, pk=adId, active=True, expires_on__gt=datetime.datetime.now())
	
	if request.method == "POST":
		form = ContactUploadForm(ad.category, request.POST, request.FILES)
		if form.is_valid():
			# send email when done
			subject = _('New response to your posting on ') + Site.objects.get_current().name
			# 1. render context to email template
			email_template = loader.get_template('contact/email/contact_ad.txt')
			context = RequestContext({'data': form.cleaned_data})
			email_contents = email_template.render(context)
			# 2. send email
			if ad.fields_dict().has_key('contactemail') and ad.fields_dict()['contactemail'] != '':
				email_address = ad.fields_dict()['contactemail']
			else:
				email_address = ad.user.email
			
			msg = EmailMessage(subject, email_contents, settings.FROM_EMAIL, [email_address])
			
			try:
				msg.attach(request.FILES['file_upload'].name, request.FILES['file_upload'].read())
			except:
				pass
			
			msg.send()
			
			# create thank you message
			try:
				request.user.message_set.create(message=_("Your message has been sent."))
			except:
				pass
			
			return HttpResponseRedirect(reverse('classifieds.adposting.views.view', args=[ad.pk]))
	else:
		form = ContactUploadForm(ad.category)
		
	return render_to_response("contact/ad.html", {'form': form}, context_instance=RequestContext(request))

