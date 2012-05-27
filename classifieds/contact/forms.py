
from django import forms
from django.utils.translation import ugettext as _

import string
import sha

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	subject = forms.CharField(max_length=64)
	message = forms.CharField(widget=forms.Textarea,label="Comments")

	def clean_captcha(self):
		# TODO check captcha... 
		return ''
	
class ContactUploadForm(ContactForm):
	file_upload = forms.FileField()

	def __init__(self, category, *args, **kwargs):
		ContactForm.__init__(self, *args, **kwargs)
		self.category = category
		if not self.category.enable_contact_form_upload:
			del self.fields['file_upload']
		else:
			extensions = str(self.category.contact_form_upload_file_extensions).split(',')
			self.fields['file_upload'].help_text = _("Your attachment must have one of the following extensions: ") + string.join(extensions, ', ') + _(" and must be smaller than ")  + str(self.category.contact_form_upload_max_size / 1024) + "KB"

	def clean_file_upload(self):
		if 'file_upload' in self.cleaned_data:
			file_upload = self.cleaned_data['file_upload']
			
			name, ext = file_upload.name.rsplit('.', 1)
			extensions = str(self.category.contact_form_upload_file_extensions).split(',')
			if ext not in extensions:
				raise forms.ValidationError(_("Your attachment must have one of the following extensions: ") + string.join(extensions, ', '))
			
			if file_upload.size > self.category.contact_form_upload_max_size:
				raise forms.ValidationError(_("Your attachment must be smaller than ") + str(self.category.contact_form_upload_max_size / 1024) + "KB")
		
	

