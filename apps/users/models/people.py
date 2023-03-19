

from django.db import models


# Defining the models. They'll be described later


# An abstract class that will contain the basic information about each person
class Person(models.Model):

    # Basic data about the person
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField('date_of_birth')

    # Security data
    email = models.EmailField()
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    security_question = models.CharField(max_length=300)
    first_login = models.DateField(auto_now_add=True)

    # Profile image field and size information
    profile_image = models.ImageField(height_field=self.image_height, width_field=self.image_width)
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    
    #
    def __str__(self):
        return self.login


#
class Role(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        abstract = True


#
class Admin(Role):
    pass


#
class Moderator(Role):
    pass


#
class Writer(Role):
    pass


#
class Reader(Role):
    pass


#
class Blocked(Role):
    pass
