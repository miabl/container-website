# Generated by Django 4.0.1 on 2022-01-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0010_unit_containers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='containers',
        ),
    ]
