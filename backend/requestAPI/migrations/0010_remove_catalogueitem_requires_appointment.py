# Generated by Django 3.2.25 on 2024-08-21 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0009_auto_20240821_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogueitem',
            name='requires_appointment',
        ),
    ]
