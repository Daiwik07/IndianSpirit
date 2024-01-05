from django.db import models
from datetime import datetime

# Create your models here.

class Sign(models.Model):
    name = models.CharField(max_length=20)
    Email = models.CharField( max_length=254,null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    date = models.DateField()
    def __str__(self):
        return self.name
    
