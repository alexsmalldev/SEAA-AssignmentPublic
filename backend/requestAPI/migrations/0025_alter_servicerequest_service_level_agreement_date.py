# Generated by Django 5.0.7 on 2024-08-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0024_servicerequest_service_level_agreement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service_level_agreement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
