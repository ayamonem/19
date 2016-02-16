from django.conf.urls import url
from django.contrib import admin
from .views import ( #more shortcuts for easy coding 
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)# u can finad more regular expresions examples here https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
	url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^list/$', post_list),
    url(r'^detail/(?P<id>\d+)/$', post_detail,name="detail"),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]
