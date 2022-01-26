from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from member.models import User
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, default=None)
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = RichTextField()
    register_date = models.DateTimeField()
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = RichTextField()
    register_date = models.DateTimeField()
    choice = models.BooleanField(default=False)