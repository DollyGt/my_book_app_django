from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=254, blank=False)
    ISBN = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    owner=models.ForeignKey(User, related_name="books", null=False)
    
    def __str__(self):
        return self.name
        