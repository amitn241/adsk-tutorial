from django.contrib import admin
from .models import *


class AuthorInline(admin.TabularInline):
    model = Author
    extra = 0 


class BookAdmin(admin.ModelAdmin):
	list_display = ('id','title','published_date') 
	inlines = (AuthorInline,)


admin.site.register(Book, BookAdmin)
