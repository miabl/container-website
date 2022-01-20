from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models

class Unit(models.Model):
    """Model representing a Unit"""
    title = models.CharField(max_length=200)

    # Foreign Key used because units can only have one coordinator, but coordinators can have multiple units
    # Coordinator as a string rather than object because it hasn't been declared yet in the file
    coordinator = models.ForeignKey('Coordinator', on_delete=models.SET_NULL, null=True)

    code = models.CharField('Code', primary_key=True, max_length=8, unique=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the unit')

    class Meta:
        ordering = ['code']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.code} ({self.title})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this unit."""
        return reverse('unit-detail', args=[str(self.id)])

class Coordinator(models.Model):
    """Model representing a coordinator"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular coordinator instance."""
        return reverse('coordinator-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'