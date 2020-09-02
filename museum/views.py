from django.shortcuts import render
from django.utils import timezone
from .models import Post, Artist, Genre, News, Dbs

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'museum/posts.html', {'posts': posts})

def genre_show(request, genre_id):
    genre = Genre.objects.all().get(id=genre_id)
    artists = genre.artist_set.all()
    return render(request, 'museum/artists.html', {'artists': artists})

def post_show(request, post_id):
    post = Post.objects.all().get(id=post_id)
    artists = post.artists.all()
    return render(request, 'museum/post_show.html', {'post': post, 'artists': artists})

def artists(request):
    artists = Artist.objects.all()
    return render(request, 'museum/artists.html', {'artists': artists})

def top(request):
    genres = Genre.objects.all()
    return render(request, 'museum/top.html', {'genres': genres})

def news(request):
    news = News.objects.all()
    return render(request, 'museum/news.html', {'newss': news})

def news_show(request, news_id):
    news = News.objects.all().get(id=news_id)
    return render(request, 'museum/news_show.html', {'news': news})

def dbs(request):
    dbss = Dbs.objects.all()
    return render(request, 'museum/dbs.html', {'dbss': dbss})

def dbs_show(request, dbs_id):
    dbs = Dbs.objects.all().get(id=dbs_id)
    return render(request, 'museum/dbs_show.html', {'dbs': dbs})