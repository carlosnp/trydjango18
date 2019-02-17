from django import forms

from .models import SingUp

class ContactForm(forms.Form):
    full_name   = forms.CharField(label="Nombre y Apeliido", required=False)
    email       = forms.EmailField()
    message     = forms.CharField(label="Mensaje")

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split("@")
    #     domain, extension = provider.split(".")
    #     # if not "edu" in email:
    #     if not domain == "gmail":
    #         raise forms.ValidationError("Use un email valido gmail")
    #     if not extension == "com":
    #         raise forms.ValidationError("Use un email valido .com")
    #     return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

class SingUpForm(forms.ModelForm):
    class Meta:
        model = SingUp
        fields = ('full_name', 'email')

    def clean_email(self):
    	email = self.cleaned_data.get('email')
    	email_base, provider = email.split("@")
    	domain, extension = provider.split(".")
    	# if not "edu" in email:
    	if not domain == "gmail":
    		raise forms.ValidationError("Use un email valido gmail")
    	if not extension == "com":
    		raise forms.ValidationError("Use un email valido .com")
    	return email

    def clean_full_name(self):
    	full_name = self.cleaned_data.get('full_name')
    	return full_name