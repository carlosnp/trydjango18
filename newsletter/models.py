from django.db import models

# Create your models here.
class SingUp(models.Model):
	email 		= models.EmailField(verbose_name='Email')
	full_name 	= models.CharField(max_length=200, blank=True, null=True,verbose_name='Nombre Completo')
	timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Creación')
	updated 	= models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Fecha de Actualización')

	class Meta:
		verbose_name='SingUp'
		verbose_name_plural='SingUps'

	def __str__(self):
		return self.email