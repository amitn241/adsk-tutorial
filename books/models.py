from django.db import models
from django.utils import timezone
from publishers.models import *
from people.models import * 


class Book(models.Model):
	title = models.CharField(max_length=100)
	secondary_title = models.CharField(max_length=100, blank=True)
	# author = models.CharField(max_length=100)
	authors = models.ManyToManyField(Person, through='Author')
	copies = models.IntegerField(default=10)
	published = models.BooleanField(default=True)
	published_date = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(decimal_places=2, max_digits=6, db_index=True)
	# publisher = models.CharField(max_length=100)
	publisher_soft = models.ForeignKey(Publisher,related_name='publisher_soft',null=True, blank=True)
	publisher_hard = models.ForeignKey(Publisher)

	def __unicode__(self):
		return self.title 


class Author(models.Model):
	person = models.ForeignKey(Person)
	book = models.ForeignKey(Book)
	order = models.IntegerField()