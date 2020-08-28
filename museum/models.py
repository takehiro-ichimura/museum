from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    movie_tag = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title