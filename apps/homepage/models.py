from django.db import models

# Create your models here.


class Link(models.Model):

    name = models.CharField(max_length=50)
    url = models.URLField()


class Image(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField()
    

class TextSection(models.Model):

    name = models.CharField(max_length=50)
    content = models.TextField()


class Keyword(models.Model):
    pass
