from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Artist, Genre, News, Dbs, Column
from .forms import CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'museum/posts.html', {'posts': posts})

def genre_show(request, genre_id):
    genre = Genre.objects.all().get(id=genre_id)
    artists = genre.artist_set.all()
    return render(request, 'museum/artists.html', {'artists': artists, 'genre': genre})

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

def columns(request):
    Columns = Column.objects.all()
    return render(request, 'museum/columns.html', {'columns': columns})

def column_show(request, dbs_id):
    Column = Column.objects.all().get(id=column_id)
    return render(request, 'museum/column_show.html', {'column': column})

def thanks(request):
    return render(request, 'museum/thanks.html')

def profile(request):
    return render(request, 'museum/profile.html')

def terms(request):
    return render(request, 'museum/terms.html')

def aboutus(request):
    return render(request, 'museum/aboutus.html')

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_show', post_id=post.pk)
    else:
        form = CommentForm()
    return render(request, 'museum/add_comment_to_post.html', {'form': form})
