from tastypie.resources import ModelResource
from tastypie import fields
from ..models import Book, Author
from people.models import Person 
# from publishers.resources.publisher import PublisherResource

class PersonResource(ModelResource):
	class Meta:
		queryset = Person.objects.all()
		resource_name = 'person'

class BookResource(ModelResource):
	# publisher_soft = fields.CharField()

	publisher_soft = fields.ForeignKey('publishers.resources.publisher.PublisherResource', 'publisher_soft', full=True)
	publisher_hard = fields.ForeignKey('publishers.resources.publisher.PublisherResource', 'publisher_hard', full=True)

	authors = fields.ToManyField(PersonResource,'authors')
	class Meta:
		queryset = Book.objects.all()
		resource_name = 'book'

		
	# def dehydrate_title(self, bundle):
	# 	return bundle.obj.title + '_GREAT'

	# def dehydrate_publisher_soft(self, bundle):
	# 	return bundle.obj.publisher_soft

	# def dehydrate(self, bundle):
	# 	bundle.data['publisher_soft']  = bundle.obj.publisher_soft
	# 	return bundle