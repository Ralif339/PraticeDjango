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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    date = models.DateField()
    duration = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.title + " " + self.name