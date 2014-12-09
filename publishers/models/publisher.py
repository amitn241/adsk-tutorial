##

from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name 

	@property 
	def books(self):
		return self.book_set.all()

	