from django.contrib.auth.models import AbstractUser, auth

from django.db import models
from django.utils import timezone
from datetime import date


class Blogger(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    bio = models.CharField(max_length=2028)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)


class Blogs(models.Model):
    title = models.CharField(max_length=300)
    date_post = models.DateField()
    author = models.ForeignKey(Blogger, related_name='blogs_set', on_delete=models.CASCADE)
    permbajtja = models.CharField(max_length=2028)


class CommenterUser(AbstractUser):
    is_blogger = models.BooleanField(default=True, null=True)
    autg= models.ForeignKey(Blogger,on_delete=models.CASCADE)

class Comment(models.Model):
    date_postc = models.DateField()
    permbajtje_c = models.CharField(max_length=2028)
    title_c = models.ForeignKey(Blogs, related_name='blog_set', on_delete=models.CASCADE)
    komentuesi = models.ForeignKey(CommenterUser, related_name='user_set', on_delete=models.CASCADE)

# 123 pass
# admin username
