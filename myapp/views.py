from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Count
from django.db import models



from django.db.models import Count

@api_view(['GET', 'POST'])
def User_all(request):
    if request.method == 'GET':
        users = User.objects.annotate(
            posts_count=Count('post', distinct=True),
            likes_count=Count('like', distinct=True),
            favorites_count=Count('favorite', distinct=True),
        )


        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
    


    
@api_view(["GET","POST"])
def post__all(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

@api_view(['GET', 'POST'])
def like__all(request):
    if request.method == 'GET':
        likes = Like.objects.select_related('user', 'post')
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    serializer = LikeSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']
        post = serializer.validated_data['post']

        if Like.objects.filter(user=user, post=post).exists():
            return Response(
                {'error': 'Ин корбар аллакай ба ин пост Like кардааст.'},
                status=400
            )

        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

    
@api_view(["GET","POST"])
def favorite__all(request):
    if request.method == 'GET':
        favorite = Favorite.objects.all()
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FavoriteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
  
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)

    if request.method in ['PUT', 'PATCH']:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    user.delete()
    return Response({'message': 'User deleted successfully'})

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = PostListSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostListSerializer(post, data=request.data)

    elif request.method == 'PATCH':
        serializer = PostListSerializer(
            post,
            data=request.data,
            partial=True
        )

    elif request.method == 'DELETE':
        post.delete()
        return Response(
            {'message': 'Post deleted successfully'}
        )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def like_detail(request, pk):
    like = Like.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    like.delete()
    return Response({"message": "Like deleted successfully"})



@api_view(['PUT', 'DELETE'])
def favorite_detail(request, pk):
    favorite = Favorite.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    favorite.delete()
    return Response({"message": "Favorite deleted successfully"})



@api_view(['PATCH'])
def user_patch(request, pk):
    user = User.objects.get (pk=pk)

    serializer = UserSerializer(user,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)




@api_view(['PATCH'])
def post_patch(request, pk):
    post = Post.objects.get(pk=pk)

    serializer = PostListSerializer(post,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)



@api_view(['PATCH'])
def like_patch(request, pk):
    like = Like.objects.get(pk=pk)

    serializer = LikeSerializer(like,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def favorite_patch(request, pk):
    favorite = Favorite.objects.get(pk=pk)

    serializer = FavoriteSerializer(favorite,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# xvcvbhjkl;
@api_view(['GET'])
def most_active_users(request):
    users = User.objects.annotate(
        posts_count=Count('post')
    ).order_by('-posts_count')[:10]

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail_get(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)




@api_view(['GET'])
def most_active_users(request):
    users = User.objects.annotate(
        posts_count=Count('post')
    ).order_by('-posts_count')[:10]

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_statistics(request):
    stats = User.objects.aggregate(
        average_age=Avg('age'),
        min_age=Min('age'),
        max_age=Max('age')
    )

    return Response({
        'total_users': User.objects.count(),
        'average_age': round(stats['average_age'], 1)
            if stats['average_age'] is not None else None,
        'min_age': stats['min_age'],
        'max_age': stats['max_age']
    })



@api_view(['GET', 'POST'])
def profile_all(request):
    if request.method == 'GET':
        profiles = Profil.objects.annotate(
            posts_count=Count('user__post', distinct=True)
        )
        serializer = ProfilSerializer(profiles, many=True)
        return Response(serializer.data)

    serializer = ProfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def profile_detail(request, pk):
    profile = get_object_or_404(Profil, pk=pk)

    if request.method == 'GET':
        serializer = ProfilSerializer(profile)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProfilSerializer(profile, data=request.data)

    elif request.method == 'PATCH':
        serializer = ProfilSerializer(
            profile, data=request.data, partial=True
        )

    if request.method in ['PUT', 'PATCH']:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    profile.delete()
    return Response({'message': 'Profile deleted successfully'})


@api_view(['GET'])
def city_statistics(request):
    cities = Profil.objects.values('city').annotate(
        users_count=Count('user', distinct=True)
    ).order_by('-users_count')

    return Response(cities)


@api_view(['GET'])
def most_active_users(request):
    users = User.objects.annotate(
        posts_count=Count('post')
    ).order_by('-posts_count')[:5]

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def users_statistics(request):
    return Response({
        'total_users': User.objects.count(),
        'total_posts': Post.objects.count(),
        'total_likes': Like.objects.count(),
        'total_favorites': Favorite.objects.count(),
    })
    
    

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.annotate(
        likes_count=Count('like', distinct=True),
        favorites_count=Count('favorite', distinct=True)
    ).select_related('user')

    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def user_posts(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserPostsSerializer(user)
    return Response(serializer.data)



@api_view(['GET'])
def popular_posts(request):
    posts = Post.objects.annotate(
        likes_count=Count('like', distinct=True)
    ).filter(
        likes_count__gte=10
    ).order_by('-likes_count')

    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_posts(request):
    q = request.GET.get('q', '')

    posts = Post.objects.filter(
        models.Q(title__icontains=q) |
        models.Q(content__icontains=q)
    )

    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_posts(request):
    posts = Post.objects.all()

    min_views = request.GET.get('min_views')
    max_views = request.GET.get('max_views')
    user_id = request.GET.get('user_id')

    if min_views:
        posts = posts.filter(viws__gte=min_views)

    if max_views:
        posts = posts.filter(viws__lte=max_views)

    if user_id:
        posts = posts.filter(user_id=user_id)

    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_statistics(request):
    stats = Post.objects.aggregate(
        total_views=Sum('viws'),
        average_views=Avg('viws'),
        max_views=Max('viws'),
        min_views=Min('viws'),
    )

    return Response({
        'total_posts': Post.objects.count(),
        'total_views': stats['total_views'] or 0,
        'average_views': stats['average_views'] or 0,
        'max_views': stats['max_views'] or 0,
        'min_views': stats['min_views'] or 0,
        'total_likes': Like.objects.count(),
        'total_favorites': Favorite.objects.count(),
    })



@api_view(['GET'])
def author_statistics(request):
    users = User.objects.annotate(
        posts_count=Count('post', distinct=True),
        total_views=Sum('post__viws'),
        average_views=Avg('post__viws'),
        likes_received=Count('post__like', distinct=True)
    )

    result = []

    for user in users:
        result.append({
            'author': {
                'id': user.id,
                'username': user.username,
                'full_name': f'{user.first_name} {user.last_name}'
            },
            'posts_count': user.posts_count,
            'total_views': user.total_views or 0,
            'average_views': user.average_views or 0,
            'likes_received': user.likes_received
        })

    return Response(result)



@api_view(['GET'])
def post_likes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    likes = Like.objects.filter(post=post).select_related('user')

    serializer = PostLikesSerializer(likes, many=True)

    return Response({
        'post_id': post.id,
        'title': post.title,
        'likes_count': likes.count(),
        'likes': serializer.data
    })



@api_view(['GET'])
def post_likes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    likes = Like.objects.filter(post=post).select_related('user')

    serializer = PostLikesSerializer(likes, many=True)

    return Response({
        'post_id': post.id,
        'title': post.title,
        'likes_count': likes.count(),
        'likes': serializer.data
    })


@api_view(['GET'])
def top_liked_posts(request):
    posts = Post.objects.annotate(
        likes_count=Count('like', distinct=True)
    ).order_by('-likes_count')[:10]

    result = []

    for post in posts:
        result.append({
            'id': post.id,
            'title': post.title,
            'author': post.user.username,
            'views': post.viws,
            'likes_count': post.likes_count
        })

    return Response(result)
