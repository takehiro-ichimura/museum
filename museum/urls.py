from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('posts/<int:post_id>', views.post_show, name="post_show"),
    path('genres/<int:genre_id>', views.genre_show, name='genre_show'),
    path('artists', views.artists, name="artists"),
    path('news', views.news, name="news"),
    path('news/<int:news_id>', views.news_show, name="news_show"),
    path('dbs', views.dbs, name="dbs"),
    path('dbs/<int:dbs_id>', views.dbs_show, name="dbs_show"),
    path('', views.top, name='top'),
]