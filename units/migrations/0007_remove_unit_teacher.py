# Generated by Django 4.0.1 on 2022-01-21 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0006_unit_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='teacher',
        ),
    ]