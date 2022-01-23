# Generated by Django 4.0.1 on 2022-01-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_lab_facilitator_lecturer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='availability',
            field=models.CharField(blank=True, choices=[('s1', 'semester 1'), ('s2', 'semester 2'), ('ss', 'summer school'), ('ns', 'non-standard teaching period'), ('os', 'offshore teaching period'), ('t1', 'trimester 1'), ('t2', 'trimester 2'), ('t3', 'trimester 3'), ('na', 'not available')], default='ns', help_text='Teaching period the unit is available', max_length=2),
        ),
    ]