# Generated by Django 5.0.7 on 2024-08-29 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0019_servicerequest_priority_servicerequest_severity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='severity',
        ),
    ]