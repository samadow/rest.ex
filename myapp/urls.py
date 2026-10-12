from django.urls import path
from .views import *

urlpatterns = [
    path('users/', User_all, name='users'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('posts/', post__all, name='posts'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('likes/', like__all, name='likes'),
    path('likes/<int:pk>/', like_detail, name='like_detail'),
    path('favorites/', favorite__all, name='favorites'),
    path('favorites/<int:pk>/', favorite_detail, name='favorite_detail'),
    path('users/<int:pk>/patch/', user_patch),
    path('posts/<int:pk>/patch/', post_patch),
    path('likes/<int:pk>/patch/', like_patch),
    path('favorites/<int:pk>/patch/', favorite_patch),
    path('users/most-active/', most_active_users, name='most_active'),  
    
]
