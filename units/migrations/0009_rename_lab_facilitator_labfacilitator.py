# Generated by Django 4.0.1 on 2022-01-21 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0008_alter_unit_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lab_facilitator',
            new_name='LabFacilitator',
        ),
    ]
