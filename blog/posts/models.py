from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=10000)        
    name = models.CharField(max_length=50, blank=True, null=True)                 
    created_at = models.DateTimeField(default=datetime.now, blank=True)