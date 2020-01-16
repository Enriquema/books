from django.db import models

# Create your models here.
class Book(models.Model): #Bookes
	id = models.AutoField(primary_key=True) #Código de Booke
	name = models.CharField(max_length=255) #nombre
	address = models.CharField(max_length=255,blank=True, null=True) #dirección
	postal_code = models.PositiveIntegerField(blank=True, null=True) #CP
	city = models.CharField(max_length=255, blank=True, null=True) #localidad
	province = models.CharField(max_length=255, blank=True, null=True) # provincia
	country = models.CharField(max_length=255, default='España', blank=True, null=True)
	fixed_telephone = models.IntegerField(blank=True, null=True) #teléfono
	mobile_telephone = models.IntegerField(blank=True, null=True) #móvil
	fax = models.IntegerField(blank=True, null=True) #fax
	email = models.EmailField(blank=True, null=True) #Email
	observations = models.TextField(blank=True, null=True) #observaciones

	# To define the way to display de Book in forms
	def __str__(self):
		return self.name
	"""docstring for Booke"""
	# def __init__(self, arg):
	# 	super(Booke,models.Model).__init__()
	# 	self.arg = arg
	#id

class Author(models.Model): #proveedores
	id = models.AutoField(primary_key=True) #Código de proveedor
	name = models.CharField(max_length=255) #nombre
	address = models.CharField(max_length=255, blank=True, null=True) #dirección
	postal_code = models.PositiveIntegerField(blank=True, null=True) #CP
	city = models.CharField(max_length=255, blank=True, null=True) #localidad
	province = models.CharField(max_length=255, blank=True, null=True) # provincia
	country = models.CharField(max_length=255, default='España', blank=True, null=True)
	fixed_telephone = models.IntegerField(blank=True, null=True) #teléfono
	mobile_telephone = models.IntegerField(blank=True, null=True) #móvil
	fax = models.IntegerField(blank=True, null=True) #fax
	email = models.EmailField(blank=True, null=True) #Email
	observations = models.TextField(blank=True, null=True) #observaciones
