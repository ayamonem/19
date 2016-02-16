from django.contrib import admin

# Register your models here.
from .models import Post
#we add the models to admin in this file
# where Post is the name of class in models.py file

admin.site.register(Post)