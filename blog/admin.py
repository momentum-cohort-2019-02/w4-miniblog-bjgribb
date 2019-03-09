from django.contrib import admin
from blog.models import Blogger, Topic, BlogPost

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Topic)
admin.site.register(Blogger)
