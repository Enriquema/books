from django.urls import path

from . import views

urlpatterns = [
	path('', views.library, name='library'),
	# Book
	path('Books', views.getBooks, name='getBooks'),
	path('Book/<int:id>/', views.getBook, name='getBook'),
	path('Book/new', views.newBook, name='newBook'),
	path('Book/edit/<int:id>', views.editBook, name='editBook'),
	# Author
	path('Authors', views.getAuthors, name='getAuthors'),
	path('Author/<int:id>/', views.getAuthor, name='getAuthor'),
	path('Author/new', views.newAuthor, name='newAuthor'),
	path('Author/edit/<int:id>', views.editAuthor, name='editAuthor'),
]