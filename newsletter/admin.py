from django.contrib import admin

# Register your models here.
from .models import SingUp

class SingUpAdmin(admin.ModelAdmin):
	list_display = ('__str__','timestamp','updated')
	class Meta:
		model = SingUp

admin.site.register(SingUp, SingUpAdmin)