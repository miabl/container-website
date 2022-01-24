from django.db import models
from django.contrib.auth.models import User
from units.models import Unit
from containers.models import ContainerInstance


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    units = models.ManyToManyField('units.Unit')
    running_container = models.OneToOneField('containers.ContainerInstance', on_delete=models.SET_NULL, null=True,
                                             blank=True)
