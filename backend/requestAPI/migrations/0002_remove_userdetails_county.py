# Generated by Django 3.2.25 on 2024-07-22 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='county',
        ),
    ]
