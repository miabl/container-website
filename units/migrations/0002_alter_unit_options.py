# Generated by Django 4.1.dev20220111112249 on 2022-01-19 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['code']},
        ),
    ]
