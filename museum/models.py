from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist)
    year = models.IntegerField(null=True)
    movie_tag = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Dbs(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
