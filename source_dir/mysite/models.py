from django.db import models

# Create your models here.
class Training(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    

class Registration(models.Model):
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    date = models.DateTimeField()
    slug = models.SlugField()
    duration = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.title