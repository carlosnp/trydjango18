from django.shortcuts import render
from .forms import SingUpForm, ContactForm
# Para enviar email
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	title = "Pagina de pruebas"
	# si esta autenticado
	if request.user.is_authenticated:
		title = "Bienvenido Usuario: %s" %(request.user)
	
	form = SingUpForm(request.POST or None)
	context = {
		"title": title,
		"abc" : 123,
		"form": form
	}

	# Formulario\
	# if request.method == "POST":
	# 	print(request.POST)
	
	# Si el formulario es valido
	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not instance.full_name:
			instance.full_name = "Nombre Completo de Prueba"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Gracias: %s" %(request.user),
			"abc": 456
		}
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# print(form.cleaned_data)
		# for key in form.cleaned_data:
		# 	print(key)
		form_email 		= form.cleaned_data.get("email")
		form_message 	= form.cleaned_data.get("message")
		form_full_name 	= form.cleaned_data.get("full_name")
		# print(email, full_name, message)

		# Enviar Email
		# subject = 'prueba de email'
		# from_email = settings.EMAIL_HOST_USER
		# to_email = [from_email, 'tucorreo@gmail.com']
		# contact_message = "%s: %s via %s"%(
		# 	form_full_name, 
		# 	form_message, 
		# 	form_email)
		# send_mail(
		# 	subject, 
		# 	contact_message, 
		# 	from_email, 
		# 	to_email,
		# 	fail_silently=False)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)
