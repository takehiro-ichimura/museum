from django.shortcuts import render
from django.utils import timezone
from .models import Post, Artist, Genre

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'museum/posts.html', {'posts': posts})

def genre_show(request, genre_id):
    genre = Genre.objects.all().get(id=genre_id)
    artists = genre.artist_set.all()
    return render(request, 'museum/artists.html', {'artists': artists})

def top(request):
    genres = Genre.objects.all()
    return render(request, 'museum/top.html', {'genres': genres})