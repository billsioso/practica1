from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author= models.CharField(max_length=100)
    body = models.TextField(default='I am the body')

    def __str__(self):
        return self.title
