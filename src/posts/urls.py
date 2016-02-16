from django.conf.urls import url
from django.contrib import admin
# u can finad more regular expresions examples here https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
    url(r'^$', "posts.views.post_home"),
]
