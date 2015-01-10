from django.contrib import admin
from blogengine.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'pubDate', 'wasPublishedRecently')

admin.site.register(Post, PostAdmin)
# Register your models here.
