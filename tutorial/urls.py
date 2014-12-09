
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from publishers.resources.publisher import PublisherResource
from books.resources.book import BookResource
# publisher_resource = PublisherResource() 


public_api = Api(api_name='public')
public_api.register(PublisherResource())
public_api.register(BookResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^book/','books.views.book'),
    url(r'^books/','books.views.books'),    
    url(r'^admin/', include(admin.site.urls)),
 	url(r'^json/','books.views.home_json'),
    url(r'api/',  include(public_api.urls)),


    url(r'task_result/','books.views.task_result'),
    url(r'', 'books.views.home'),


 )

 
