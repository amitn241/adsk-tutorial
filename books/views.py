# from django.shortcuts import render

from celery.result import AsyncResult
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
from django.conf import settings
from .models import *
from .tasks import add
import json 

def home(request):
	ar = add.delay(5,8)
	# ar.get()
	return HttpResponse("<htmL><body><h1>Welcome to my store</h1><h2>Task ID: %s %s</h2></body></html>" % (ar.id, ar.status))


def task_result(request):
	task_id = request.GET.get('task')
	result = AsyncResult(task_id)
	if result.ready():
		data = result.get()
		return HttpResponse("<htmL><body><h1>Result: %s</h1></body></html>" % data)
	else:
		return HttpResponse("<htmL><body><h1>Not Ready</h1></body></html>")

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










