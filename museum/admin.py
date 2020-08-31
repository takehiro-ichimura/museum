from django.contrib import admin
from .models import Post, Artist, Genre

# Register your models here.
admin.site.register(Post)
admin.site.register(Artist)
admin.site.register(Genre)
