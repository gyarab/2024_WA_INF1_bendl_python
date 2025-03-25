from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo =  models.ImageField(upload_to='logos/')
    preview = models.ImageField(upload_to='previews/', default=None, null=True)
    genre = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")  # Vazba 1:N
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automaticky nastaví čas při vytvoření
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # IP adresa uživatele
    user_agent = models.TextField(null=True, blank=True)  # User Agent uživatele

    def __str__(self):
        return f"Komentář k {self.game.name} ({self.created_at})"