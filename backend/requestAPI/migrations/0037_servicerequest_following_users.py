# Generated by Django 3.2.25 on 2024-09-12 14:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requestAPI', '0036_alter_building_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='following_users',
            field=models.ManyToManyField(blank=True, related_name='service_request', to=settings.AUTH_USER_MODEL),
        ),
    ]
