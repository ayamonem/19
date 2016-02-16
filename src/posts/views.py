from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# we will create CRUD(Create ,Retreve,Update,Delete)
def post_create(request):
	#return HttpResponse("<h1>Create</h1>")
	return render(request, "index.html", {}) #we are calling template --> {} from settings file 
def post_detail(request):#for retreve
	return HttpResponse("<h1>Detail</h1>")
def post_list(request):#for list items
	return HttpResponse("<h1>List</h1>")
def post_update(request):
	return HttpResponse("<h1>Update</h1>")
def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")