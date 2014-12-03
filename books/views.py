# from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
from django.conf import settings
from .models import *

import json 

def home(request):
	return HttpResponse("<htmL><body><h1>Welcome to my store</h1></body></html>")


def home_json(request):
	data = {
		'store_name' : 'Great Store',
		'open' : True
	}

	s = json.dumps(data)

	return HttpResponse(s,content_type="application/json")


def book(request):

	book_index = request.GET.get('book_index',settings.BOOK_INDEX)


	# tmpl =   template.Template("<html><body> \
	# 	<div>Title: {{title}}</div> \
	# 	<div>Author: {{author}}</div> \
	# </body></html>")

	tmpl = get_template('books.html')

	try:
		book_index = int(book_index)
		book = Book.objects.get(pk=book_index)

	except Book.DoesNotExist:
		return HttpResponse("Book Does Not Exist")
	except:
		return HttpResponse("General Error")

	return render_to_response('books.html',{'book' : book })

def books(request):
	tmpl = get_template('book_list.html')
	c = template.Context({ 'books' : Book.objects.all() })
	return HttpResponse(tmpl.render(c))










