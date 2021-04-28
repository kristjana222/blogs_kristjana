from django.contrib import admin
from .models import Blogger, Blogs, CommenterUser, Comment, AbstractUser

# Register your models here.
admin.site.register(Blogger)
admin.site.register(Blogs)
admin.site.register(CommenterUser)
admin.site.register(Comment)
