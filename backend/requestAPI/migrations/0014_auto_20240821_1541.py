# Generated by Django 3.2.25 on 2024-08-21 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0013_alter_catalogueitem_buildings'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='update',
            name='title',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='comment',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='service_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='requestAPI.servicerequest'),
        ),
    ]