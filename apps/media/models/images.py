

from django.db import models


class Image(models.Model):
    
    # Information about the image
    title = models.CharField(max_length=150)
    source = models.CharField(max_length=300)

    # Place where the image should be stored
    upload_directory = ''

    # The field in which the image data will be stored
    image = models.ImageField(upload_to=upload_directory)

    class Meta:
        abstract = True


class Banner(Image):
    
    # Banners will be stored inside the media/banners
    upload_directory = 'banners/'


class ProfilePicture(Image):
    pass


class BlogPostImage(Image):
    pass
