

from django.db import models
from people import Person

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
