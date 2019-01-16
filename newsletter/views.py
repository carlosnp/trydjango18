from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Pagina de pruebas"
	if request.user.is_authenticated:
		title = "Bienvenido Usuario: %s" %(request.user)
	context = {
		"title": title,
		"abc" : 123,
	}
	return render(request, "home.html", context)