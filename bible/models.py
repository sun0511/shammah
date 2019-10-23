from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    text = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)