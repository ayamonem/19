from django.contrib import admin

# Register your models here.
from .models import Post
#we add the models to admin in this file
# where Post is the name of class in models.py file

# now we will cusmoize Admin by adding more options like adding Timestamp,updated Column,adding filter date also
#u can find more admin options here https://docs.djangoproject.com/en/1.9/ref/contrib/admin/
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","content","updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]  #this is filter function for date

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)