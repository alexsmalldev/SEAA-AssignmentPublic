# Generated by Django 5.0.7 on 2024-09-05 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestAPI', '0031_alter_update_associated_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CatalogueItem',
            new_name='ServiceType',
        ),
    ]
