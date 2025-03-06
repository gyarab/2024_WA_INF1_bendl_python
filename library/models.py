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