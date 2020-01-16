from django import forms
from .models import Book
from .models import Author

class BookForm(forms.ModelForm):
	# CSS config
	error_css_class = 'error'
	required_css_class = 'required'

	class Meta:
		model = Book
		fields = ('name','address','postal_code','city','province','country','fixed_telephone','mobile_telephone','fax','email','observations')
		# Styling
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'province': forms.TextInput(attrs={'class': 'form-control'}),
			'country': forms.TextInput(attrs={'class': 'form-control'}),
			'fixed_telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'mobile_telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'fax': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'observations': forms.TextInput(attrs={'class': 'form-control'}),
		}

class AuthorForm(forms.ModelForm):
	# CSS config
	error_css_class = 'error'
	required_css_class = 'required'

	class Meta:
		model = Author
		fields = ('name','address','postal_code','city','province','country','fixed_telephone','mobile_telephone','fax','email','observations')
		# Styling
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'province': forms.TextInput(attrs={'class': 'form-control'}),
			'country': forms.TextInput(attrs={'class': 'form-control'}),
			'fixed_telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'mobile_telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'fax': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'observations': forms.TextInput(attrs={'class': 'form-control'}),
		}
