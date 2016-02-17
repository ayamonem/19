"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
# u can finad more regular expresions examples here https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
# u can see how to setup static files in https://docs.djangoproject.com/en/1.9/howto/static-files/
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)