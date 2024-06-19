from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creation_date =  models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default='new') # e.g new, posted, draft
    post_title = models.CharField(max_length=32)
    post_type = models.CharField(max_length=32) # e.g post, project, about, page
    post_content = models.TextField(null=True)
    post_parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)


class PostMeta(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, null=True)
    value = models.TextField(null=True)

