# Generated by Django 3.2.25 on 2024-08-21 14:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requestAPI', '0008_building_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceRequestItem',
            new_name='CatalogueItem',
        ),
        migrations.RenameModel(
            old_name='ServiceRequestComment',
            new_name='Update',
        ),
    ]
