# Generated by Django 5.0.7 on 2024-08-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0022_alter_servicerequest_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='open', max_length=20),
        ),
    ]
