# Generated by Django 4.1.dev20220111112249 on 2022-01-19 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Code')),
                ('summary', models.TextField(help_text='Enter a brief description of the unit', max_length=1000)),
                ('coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='units.coordinator')),
            ],
        ),
    ]
