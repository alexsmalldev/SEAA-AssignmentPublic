# Generated by Django 3.2.25 on 2024-09-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0045_alter_servicerequest_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
