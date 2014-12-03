from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^book/','books.views.book'),
    url(r'^books/','books.views.books'),    
    url(r'^admin/', include(admin.site.urls)),
 	url(r'^json/','books.views.home_json'),
    url(r'', 'books.views.home'),



 )

 
