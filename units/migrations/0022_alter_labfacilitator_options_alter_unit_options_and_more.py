# Generated by Django 4.0.1 on 2022-01-24 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units', '0021_alter_lecturer_options_remove_lecturer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labfacilitator',
            options={},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['code'], 'permissions': (('can_edit_unit', 'Edit Unit'), ('can_edit_teachers', 'Change Teachers'))},
        ),
        migrations.RemoveField(
            model_name='labfacilitator',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='labfacilitator',
            name='last_name',
        ),
        migrations.AddField(
            model_name='labfacilitator',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
