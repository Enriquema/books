from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Create your views here.
def library(request):
	# template = loader.get_template('../templates/admin/base.html')
	# context = {
	# 	'all_albums': 'all_albums',
	# }
	return render(request,'library/index.html')

########################### Book ###########################
from .forms import BookForm
from .models import Book

def getBooks (request):
	# OJO Book.objects is not a list
	Books_list = Book.objects.order_by('id') #.filter.order_by()...
	return render(request,'library/getObjects.html', {'Books_list': Books_list})

def getBook (request,id):
	Book = get_object_or_404(Book, id=id)
	return render(request,'library/getObject.html', {'Book': Book})

def newBook (request):
	# messages.info(request, 'Your password has been changed successfully!')
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			Book = form.save() # Se guarda y se obtiene el id para poder redirigir
			return redirect('getObject', id=Book.id)
		else:
			return render(request,'library/editBook.html',{'form':form})
	else:
		form = BookForm() ## Se define el formulario a utilizar
	return render(request,'library/newObject.html',{'form':form})

def editBook (request,id):
	Book = get_object_or_404(Book, id=id)
	# messages.info(request, 'Your password has been changed successfully!')
	if request.method == 'POST':
		form = BookForm(request.POST)
		pdb.set_trace()
		if request.POST.get('delete'): # Se obtiene el input con el name "delete", si se ha hecho post con este, se elimina y se manda al grid
			Book.delete()
			return redirect('getObjects')
		elif form.is_valid():
			Book = form.save() # Se guarda y se obtiene el id para poder redirigir
			return redirect('getObject', id=Book.id)
	else:
		form = BookForm(instance=Book) ## Se define el formulario a utilizar
	return render(request,'library/editBook.html',{'form':form})

def removeBook (request, id):
	Book = get_object_or_404(Book, id=id)
	Book.delete()
	return redirect('getObjects')

########################### Author ###########################
from .forms import AuthorForm
from .models import Author

def getAuthors (request):
	# OJO Author.objects is not a list
	Authors_list = Author.objects.order_by('id') #.filter.order_by()...
	return render(request,'library/getObjects.html', {'Authors_list': Authors_list})

def getAuthor (request,id):
	Author = get_object_or_404(Author, id=id)
	return render(request,'library/getObject.html', {'Author': Author})

def newAuthor (request):
	# messages.info(request, 'Your password has been changed successfully!')
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			Author = form.save() # Se guarda y se obtiene el id para poder redirigir
			return redirect('getObject', id=Author.id)
		else:
			return render(request,'library/editObject.html',{'form':form})
	else:
		form = AuthorForm() ## Se define el formulario a utilizar
	return render(request,'library/newObject.html',{'form':form})

def editAuthor (request,id):
	Author = get_object_or_404(Author, id=id)
	# messages.info(request, 'Your password has been changed successfully!')
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		pdb.set_trace()
		if request.POST.get('delete'): # Se obtiene el input con el name "delete", si se ha hecho post con este, se elimina y se manda al grid
			Author.delete()
			return redirect('getObjects')
		elif form.is_valid():
			Author = form.save() # Se guarda y se obtiene el id para poder redirigir
			return redirect('getObject', id=Author.id)
	else:
		form = AuthorForm(instance=Author) ## Se define el formulario a utilizar
	return render(request,'library/editObject.html',{'form':form})

def removeAuthor (request, id):
	Author = get_object_or_404(Author, id=id)
	Author.delete()
	return redirect('getObjects')
