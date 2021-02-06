from django.contrib import admin
from .models import Post, Artist, Genre, News, Dbs, Comment, Column, GenreOfColumn

# Register your models here.
admin.site.register(Post)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(News)
admin.site.register(Dbs)
admin.site.register(Column)
admin.site.register(Comment)
admin.site.register(GenreOfColumn)