from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title' ,'text', 'created_At', 'updated_At']

admin.site.register(Post, PostAdmin)