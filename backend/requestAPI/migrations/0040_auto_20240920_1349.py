# Generated by Django 3.2.25 on 2024-09-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0039_auto_20240920_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_level_agreement_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
