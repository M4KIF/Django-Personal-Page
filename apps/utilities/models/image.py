

from django.db import models


#
class Image(models.Model):
    
    #
    name = models.CharField(max_length=50)
    
    #
    height = models.IntegerField()
    
    #
    width = models.IntegerField()

    #
    image = models.ImageField(upload_to='images/')

