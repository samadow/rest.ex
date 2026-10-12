from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    age = models.IntegerField()
    cr_at = models.DateField(auto_now_add=True)
    
class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField( max_length=50)
    city = models.CharField(max_length=50)
    birz_date = models.IntegerField()
    avatar = models.FileField(upload_to='avatars/', max_length=100)
    
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title =models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    viws = models.IntegerField()
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.IntegerField()
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=False, auto_now_add=False)
    
    
class Favorite(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateField( auto_now_add=True)
    