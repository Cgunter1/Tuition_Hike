from django import forms

class ContactForm(forms.Form):
	"""This is the class for the contact form that people would send"""
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)