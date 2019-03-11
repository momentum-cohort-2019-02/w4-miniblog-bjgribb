from django.contrib import admin
from blog.models import Blogger, Topic, BlogPost, BlogPostDetail

# Register your models here.

# Define the admin Blogger class
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','bio')

# Define the admin Blogpost class
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'blogger', 'display_topic', 'post_date')


class BlogPostDetailAdmin(admin.ModelAdmin):
    list_filter = ('inappropriate_content')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Topic)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(BlogPostDetail)
