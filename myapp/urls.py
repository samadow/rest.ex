
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

]
