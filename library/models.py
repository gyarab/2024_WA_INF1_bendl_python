from django.db import models
from django.contrib.auth.models import User

#---------------------Categories---------------------#
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#---------------------Authors------------------------#   
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Game(models.Model):
    name  = models.CharField (max_length=100)
    genre = models.ManyToManyField(Genre)
    autor = models.ManyToManyField(Author)
    logo      = models.ImageField(upload_to = 'logos'  , default='logos/default_logo.png')
    preview   = models.ImageField(upload_to = 'previews/', default='previews/default_previews.png')
    thumbnail = models.ImageField(upload_to = 'thumbnails/', default='thumbnails/default_thumbnail.png')
    code_path = models.CharField(blank=True, null=True)
    descript  = models.TextField(blank=True, null=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_games', blank=True)
    
    def __str__(self):
        return self.name
    
#---------------------Comments-----------------------#   
class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")  
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    def __str__(self):
       return f"Komentář k {self.game.name} ({self.created_at})"