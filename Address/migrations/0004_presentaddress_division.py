# Generated by Django 4.1.2 on 2023-01-18 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0003_rename_policestation_presentaddress_upazila'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentaddress',
            name='Division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.division'),
        ),
    ]