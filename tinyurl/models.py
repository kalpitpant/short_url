from django.db import models
from django.db.models import Model 
# Create your models here.

class ShortURL(models.Model):
    original_website = models.URLField(max_length = 200)
    shortcut_url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.original_website+" "+self.shortcut_url


class Choice(models.Model):

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)