# Generated by Django 4.1.2 on 2023-01-18 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0002_postcode_upazila_presentaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presentaddress',
            old_name='PoliceStation',
            new_name='Upazila',
        ),
    ]