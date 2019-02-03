from django.shortcuts import render
from .forms import SingUpForm, ContactForm
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
		instance.save()
		context = {
			"title": "Gracias: %s" %(request.user),
			"abc": 456
		}
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)