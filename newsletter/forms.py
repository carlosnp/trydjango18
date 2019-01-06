from django import forms

from .models import SingUp

class SingUpForm(forms.ModelForm):
    class Meta:
        model = SingUp
        fields = ('full_name', 'email')

    def clean_email(self):
    	email = self.cleaned_data.get('email')
    	email_base, provider = email.split("@")
    	domain, extension = provider.split(".")
    	# if not "edu" in email:
    	if not domain == "code":
    		raise forms.ValidationError("Use un email valido CODE")
    	if not extension == "edu":
    		raise forms.ValidationError("Use un email valido .edu")
    	return email

    def clean_full_name(self):
    	full_name = self.cleaned_data.get('full_name')
    	return full_name