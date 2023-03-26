

from django.db import models

from enum import Enum

from misc import Link


###################
# Buttons section #
###################


class SettingsButtonsManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('setting'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('setting'))


class ExternalLinkButtonManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('external_link'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('external_link'))


class InternalLinkButtonManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('internal_link'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('internal_link'))


class CTAButtonManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('call_to_action'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('call_to_action'))


class MenuButtonManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('menu_button'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('menu_button'))


class TextRefferenceButtonManager(models.Manager):

    #
    def create_button(self, name):
        button = self.create(button_type=self.BUTTON_TYPE.get_value('text_refference'), name=name)

        return button

    def get_queryset(self):
        return super().get_queryset().filter(button_type=self.BUTTON_TYPE.get_value('text_refference'))


# Contains the baseplate for a button that will later be defined inside the html template.
class Button(Link):

    # The options of the button functionality
    class BUTTON_TYPE(Enum):
        setting = ('S', 'display/looks etc. options')
        external_link = ('E', 'External-link')
        internal_link = ('I', 'Internal-link')
        call_to_action = ('C', 'Call-to-action')
        menu_button = ('M', 'Menu-button')
        text_refference = ('R', 'Text-refference')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    button_type = models.CharField(
            max_length=1,
            choices=[x.value for x in BUTTON_TYPE],
            default=BUTTON_TYPE.get_value('call_to_action')
            )
 
    # The name that the button will display
    name = models.CharField(
        max_length = 50,
        null = True
            )

    # Custom managers for the button objects
    settings = SettingsButtonsManager()
    external_links = ExternalLinkButtonManager()
    internal_links = InternalLinkButtonManager()
    calls_to_actions = CTAButtonManager()
    menu_buttons = MenuButtonManager()
    text_refferences = TextRefferenceButtonManager()

    #

    def __str__(self):
        return self.button_type


    def get_absolute_url(self):
        return '/%s/' % self.name


#################
# Menu section #
#################

#
class MenuManager(models.Manager):

    # Instantiating method
    def create_menu(self, type, name, toggle_button):
        
        # Creating the menu object
        menu = self.create(type=type, name=name, toggle_button=toggle_button)
        
        # And returning it
        return menu


# A menu model that has a many to many relation with buttons, to be exact, any menu can store any amount of buttons
class Menu(models.Model):

    # Stores all of the available types of menus
    MENU_TYPE = (
        ('H', 'Hamburger'),
        ('S', 'Side'),
        ('D', 'Dropdown'),
        ('N', 'Navbar'),
            )
    
    # Stores the type of this menu
    type = models.CharField(
            max_length = 1,
            choices = MENU_TYPE,
        )

    # The name that the menu will be given. "Settings" for example
    name = models.CharField(
        max_length=50,
        null=True
            )
    
    # Stores the the relation to a button that is used for displaying the menu
    toggle_button = models.ForeignKey(
        Button,
        models.SET_NULL,
        blank = True,
        null = True,
            )

    # Buttons that the menu will contain
    menu_buttons = models.ManyToManyField(
        Button,
            )
    
    #

    def __str__(self):
        return self.name

#
# Navbar section #
#

#
class Navbar(models.Model):

    NAVBAR_LOCATIONS = (
        ('H', 'Home'),
        ('B', 'Blog'),
            )

    # Describes to which part of the app does the Navbar belong
    location = models.CharField(
            max_length = 1,
            choices = NAVBAR_LOCATIONS
            )


    # Storing the buttons that the navbar can contain
    buttons = models.ManyToManyField(
            Button,
            )
    
    # Storing the menus that the navbar can contain
    menus = models.ManyToManyField(
            Menu,
            )
