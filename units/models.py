from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
    """Model representing a Unit - a class"""
    title = models.CharField(max_length=200)

    # primary_key=True & unique=True - the primary key for model must be different for every unit
    code = models.CharField('Code', primary_key=True, max_length=8, unique=True, help_text='4 letter & 4 digit Unit Code <a href="https://handbooks.uwa.edu.au//search">UWA handbook</a>')

    # Foreign key - unit has only one coordinator but coordinator can have many units
    # null=False - unit must have coordinator
    # on_delete=models.PROTECT - so can't delete coordinator until unit is deleted
    # coordinator = models.ForeignKey('Coordinator', on_delete=models.PROTECT, null=False)
    coordinator = models.ForeignKey('Coordinator', on_delete=models.SET_NULL, null=True)
    # Lecturer can have many units & units can have many lecturers
    lecturer = models.ManyToManyField('Lecturer')
    # Can have many facilitators & facilitators can have many units
    lab_facilitator = models.ManyToManyField('lab_facilitator')

    # Description of unit
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the unit')

    # teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    OFFERING = (
        ('s1', 'semester 1'),
        ('s2', 'semester 2'),
        ('ss', 'summer school'),
        ('ns', 'non-standard teaching period'),
        ('os', 'offshore teaching period'),
        ('t1', 'trimester 1'),
        ('t2', 'trimester 2'),
        ('t3', 'trimester 3'),
        ('na', 'not available')
    )

    availability = models.CharField(
        max_length=2,
        choices=OFFERING,
        blank=True,
        default='ns',
        help_text='Teaching period the unit is available',
    )

    class Meta:
        ordering = ['code']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.code} ({self.title})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this unit."""
        return reverse('unit-detail', args=[str(self.code)])

class Coordinator(models.Model):
    """Model representing a coordinator"""
    title = models.CharField(max_length=10, default = 'Dr.', help_text='E.g. Dr. Prof. Mr.')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular coordinator instance."""
        return reverse('coordinator-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Lecturer(models.Model):
    """Model representing a coordinator"""
    title = models.CharField(max_length=10, default = 'Dr.', help_text='E.g. Dr. Prof. Mr.')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular coordinator instance."""
        return reverse('lecturer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class lab_facilitator(models.Model):
    """Model representing a coordinator"""
    title = models.CharField(max_length=10, default = 'Dr.', help_text='E.g. Dr. Prof. Mr.')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular coordinator instance."""
        return reverse('lab_facilitator-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'