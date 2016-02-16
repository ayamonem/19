from django.conf.urls import url
from django.contrib import admin
from . import views
# u can finad more regular expresions examples here https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
	url(r'^$', "posts.views.post_create"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^list/$', "posts.views.post_list"),
    url(r'^delete/$', "posts.views.post_delete"),
    url(r'^update/$', "posts.views.post_update"),

]
