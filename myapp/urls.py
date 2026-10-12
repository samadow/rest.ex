
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', User_all, name='users'),
    path('users/most-active/', most_active_users),
    path('users/statistics/', user_statistics),
    path('users/<int:pk>/', user_detail),
    path('users/<int:pk>/detail/', user_detail_get),
    path('posts/', post_list, name='posts'),
    path('likes/', like__all),
    path('likes/<int:pk>/', like_detail),
    path('favorites/', favorite__all),
    path('favorites/<int:pk>/', favorite_detail),
    path('profiles/', profile_all, name='profiles'),
    path('profiles/city-statistics/', city_statistics, name='city_statistics'),
    path('profiles/<int:pk>/', profile_detail, name='profile_detail'),
    path('users/most-active/',most_active_users,name='most_active_users'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('users/<int:pk>/posts/', user_posts, name='user_posts'),
    path('posts/popular/', popular_posts, name='popular_posts'),
    path('posts/search/', search_posts, name='search_posts'),
    path('posts/filter/', filter_posts, name='filter_posts'),
    path('posts/statistics/', post_statistics, name='post_statistics'),
    path('posts/author-statistics/',author_statistics,name='author_statistics'),
    path('posts/<int:pk>/likes/', post_likes, name='post_likes'),
    path('posts/<int:pk>/likes/', post_likes, name='post_likes'),
    path('likes/top-posts/', top_liked_posts, name='top_liked_posts'),



]
