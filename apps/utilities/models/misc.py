

from django.db import models


# Describes a link, either internal or external
class Link(models.Model):

    # Stores the types of the URL that the link can store
    LINK_TYPE = (
        ('I', 'Internal'),
        ('E', 'External'),
            )

    # Contains the information about the url 
    type = models.CharField(
            max_length=1,
            choices=LINK_TYPE,
            )
    
    # Stores the url
    url_adress = models.URLField(
        null = True,
        blank = True
            )

    class Meta:
        abstract = True
