from django.db import models
from django.urls import reverse
from .start_container import spawn_container


class Container(models.Model):
    """A class containing information about the containers stored on AWS"""

    # Fields
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the container')
    instructions = models.TextField(max_length=1000, help_text='Enter any instructions required for the container')
    flag = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """ String for representing the container object """
        return self.name

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this container."""
        return reverse('container-detail', args=[str(self.id)])


class ContainerInstance(models.Model):
    """ A class containing information about one instance of a container"""
    container = models.ForeignKey('Container', on_delete=models.CASCADE)
    containerARN = models.CharField(max_length=2048)
    public_ip = models.CharField(max_length=15)

    def get_absolute_url(self):
        """ Returns the url to access a detail record of the container instance """
        return reverse('container-instance-detail', args=[str(self.id)])
