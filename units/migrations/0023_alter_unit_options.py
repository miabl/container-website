# Generated by Django 4.0.1 on 2022-01-24 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0022_alter_labfacilitator_options_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['code'], 'permissions': (('can_edit_unit', 'Can Edit Unit'), ('can_edit_teachers', 'Can Change Teachers'))},
        ),
    ]