
from rest_framework import serializers
from .models import User, Post, Like, Favorite,Profil
from django.db.models import Sum


from rest_framework import serializers
from .models import User, Profil, Post, Like, Favorite
from django.shortcuts import get_object_or_404
from django.db.models import Count, Avg, Min, Max,Sum


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    posts_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    favorites_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = [ 'id', 'username', 'first_name', 'last_name', 'full_name', 'age', 'posts_count', 'likes_count', 'favorites_count']

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    statistics = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'full_name',
            'age', 'profile', 'statistics'
        ]

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def get_profile(self, obj):
        profile = Profil.objects.filter(user=obj).first()

        if profile:
            return {
                'bio': profile.bio,
                'city': profile.city
            }

        return None

    def get_statistics(self, obj):
        posts = Post.objects.filter(user=obj)

        return {
            'posts_count': posts.count(),
            'total_views': posts.aggregate(
                total=Sum('viws')
            )['total'] or 0,
            'likes_received': Like.objects.filter(
                post__user=obj
            ).count(),
            'favorites_received': Favorite.objects.filter(
                post__user=obj
            ).count()
        }

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),source='user',write_only=True)

    class Meta:
        model = Post
        fields = '__all__'



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        
        

class UserDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    statistics = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'full_name',
            'age', 'profile', 'statistics'
        ]

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def get_profile(self, obj):
        profile = Profil.objects.filter(user=obj).first()

        if profile:
            return {
                'bio': profile.bio,
                'city': profile.city
            }

        return None

    def get_statistics(self, obj):
        posts = Post.objects.filter(user=obj)
        

        return {
            'posts_count': posts.count(),
            'total_views': posts.aggregate(
                total=__import__('django.db.models', fromlist=['Sum']).Sum('viws')
            )['total'] or 0,
            'likes_received': Like.objects.filter(post__user=obj).count(),
            'favorites_received': Favorite.objects.filter(post__user=obj).count()
        }



class ProfileUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name']

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class ProfilSerializer(serializers.ModelSerializer):
    user = ProfileUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profil
        fields = [
            'id', 'user', 'user_id', 'bio',
            'city', 'birz_date', 'avatar', 'posts_count'
        ]
