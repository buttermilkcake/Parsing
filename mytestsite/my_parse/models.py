from django.db import models

from django.urls import reverse 
# Used to generate URLs by reversing the URL patterns

class Message(models.Model):
    """Model representing a message."""
    type = models.CharField(max_length=200, help_text='Enter a type of message you would like to see a total of (e.g. symbol clear)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.type
