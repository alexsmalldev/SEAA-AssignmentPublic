# Generated by Django 3.2.25 on 2024-09-10 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requestAPI', '0033_alter_building_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='title',
        ),
        migrations.AlterField(
            model_name='building',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='buildings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestAPI.building'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='service_icon',
            field=models.ImageField(upload_to='service_icons/'),
        ),
    ]