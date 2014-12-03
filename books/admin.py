from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ('id','title','published_date') 


admin.site.register(Book, BookAdmin)
