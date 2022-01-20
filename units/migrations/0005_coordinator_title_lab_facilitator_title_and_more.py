# Generated by Django 4.0.1 on 2022-01-20 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_unit_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='title',
            field=models.CharField(default='Dr.', help_text='E.g. Dr. Prof. Mr.', max_length=10),
        ),
        migrations.AddField(
            model_name='lab_facilitator',
            name='title',
            field=models.CharField(default='Dr.', help_text='E.g. Dr. Prof. Mr.', max_length=10),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='title',
            field=models.CharField(default='Dr.', help_text='E.g. Dr. Prof. Mr.', max_length=10),
        ),
    ]
