from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','slug','author','publish','status']
	list_filter = ['status','publish','author','created']
	search_fields = ['title','body']
	prepopulated_fields = {'slug':('title',)}
	ordering = ['status','publish']
	date_hierarchy = 'publish'
	raw_id_fields = ['author']