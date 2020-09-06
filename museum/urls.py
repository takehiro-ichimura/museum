from django.urls import path
from django.shortcuts import redirect
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
    path('columns', views.columns, name="columns"),
    path('columns/<int:dbs_id>', views.column_show, name="column_show"),
    path('thanks', views.thanks, name='thanks'),
    path('profile', views.profile, name='profile'),
    path('terms', views.terms, name='terms'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('', views.top, name='top'),
    path('posts/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]