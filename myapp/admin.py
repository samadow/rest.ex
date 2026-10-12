from django.contrib import admin
from .models import User, Profil, Post, Like, Favorite

admin.site.register([User, Profil, Post, Like, Favorite])