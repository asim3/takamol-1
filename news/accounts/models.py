from django.db import models
from django.contrib.auth.models import User


class Favorite(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    url = models.SlugField(max_length=500, blank=True, null=True)
    urlToImage = models.SlugField(max_length=500, blank=True, null=True)
    publishedAt = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
