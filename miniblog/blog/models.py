from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

