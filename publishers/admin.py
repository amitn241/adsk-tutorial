from django.contrib import admin
from .models import Publisher
from books.models import Book

# Register your models here.

class BookInline(admin.TabularInline):
	model = Book
	fk_name = 'publisher_hard'
	extra = 0


class PublisherAdmin(admin.ModelAdmin):
	list_display=('name','address')
	inlines = (BookInline,)

admin.site.register(Publisher, PublisherAdmin)