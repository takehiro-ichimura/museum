from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('genres/<int:genre_id>', views.genre_show, name='genre_show'),
    path('', views.top, name='post_list'),
]