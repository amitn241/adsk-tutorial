from django.db import models

# Create your models here.

class Person(models.Model):

	SEX_CHOICES = (
		(0, 'Unknown'),
		(1, 'Male'),
		(2, 'Female')
	)

	ssn = models.CharField(primary_key=True,max_length=12)
	phone_number = models.CharField(unique=True,max_length=10)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.PositiveIntegerField(default=0)
	sex = models.IntegerField(choices=SEX_CHOICES)


	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

	@classmethod
	def generate(cls):
		pass

	def full_clean(self,exclude=None, validate_unique=True):
		# import pdb; pdb.set_trace()
		if self.pk=='':
			self.ssn = '%s' % (self.__class__._default_manager.all().count()+1000)
			super(self.__class__, self).full_clean(exclude,validate_unique)

	def save(self, *args, **kwargs):
		self.full_clean()
		super(self.__class__, self).save(*args, **kwargs)




# def print_list(l):
# 	print l


# def print_list(*l):
# 	print l 


# print_list([1,2,3,4,5])

# print_list(1,2,3,4,5)


# print_dict(data):
# 	print data.keys() 

# print_dict(**data):
# 	print data.keys() 

# d = {'name':'amit','age':12}

# print_dict(d)

# print_dict(**d)

