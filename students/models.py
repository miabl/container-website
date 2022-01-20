from django.db import models
from django.contrib.auth.models import User
from units.models import Unit


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    units = models.ManyToManyField('units.Unit')

# Create your models here.
