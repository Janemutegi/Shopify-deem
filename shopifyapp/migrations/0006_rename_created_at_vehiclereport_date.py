# Generated by Django 5.0.7 on 2024-12-04 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyapp', '0005_rename_newsletters_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclereport',
            old_name='created_at',
            new_name='date',
        ),
    ]
