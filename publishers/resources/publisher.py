

from tastypie.resources import ModelResource 
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from ..models import Publisher 


class AnnoymousAuthorization(Authorization):
    def delete_detail(self, object_list, bundle):
       return True

    def read_detail(self, object_list, bundle):
    	return True

    def read_list(self, object_list, bundle):
    	return object_list



class PublisherResource(ModelResource):
	class Meta:
		queryset = Publisher.objects.all()
		resource_name = 'publisher' 
		include_resource_uri = True
		always_return_data = True
		#excludes = ['address']
		# authorization = AnnoymousAuthorization()
		ordering=['id','name']
		filtering = {
			'name' : ('exact'),
			'address' : ('exact','startswith',)
		}


