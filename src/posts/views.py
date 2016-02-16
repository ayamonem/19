from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

# we will create CRUD(Create ,Retreve,Update,Delete)
def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):#for retreve
	instance=get_object_or_404(Post,id=1)
	context={"title": instance.title,"instance": instance}
	return render(request, "post_detail.html", context) #we are calling template --> {} from settings file 

def post_list(request):#for list items
	queryset = Post.objects.all()
	context={"title":"List","object_list":queryset}
	return render(request, "index.html", context) #we are calling template --> {} from settings file 

def post_update(request):
	return HttpResponse("<h1>Update</h1>")
def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")