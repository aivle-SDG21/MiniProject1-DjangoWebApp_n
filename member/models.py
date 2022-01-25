from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser) :
    user_type = models.IntegerField(default=0)
    nickname = models.CharField(blank=True, max_length=50)
    user_photo = models.ImageField(blank=True)

class Write(models.Model) :
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    file_path = models.CharField(max_length=100)
    make_time = models.DateTimeField()
    update_time = models.DateTimeField()
    photo = models.ImageField()
    tag = models.CharField(max_length=50)
    count = models.IntegerField()
    like = models.IntegerField()
    solved = models.IntegerField(default=0)

class Comment(models.Model) :
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=5000)
    file = models.CharField(max_length=100)
    make_time = models.DateTimeField()
    update_time = models.DateTimeField()
    choice = models.IntegerField(default=0)
    write = models.ForeignKey(
        Write, on_delete=models.SET_NULL, null=True
    )
