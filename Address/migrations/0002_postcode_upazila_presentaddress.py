# Generated by Django 4.1.2 on 2023-01-22 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcode',
            name='Upazila',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.upazila'),
        ),
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersionName', models.CharField(blank=True, max_length=200, null=True)),
                ('Address1', models.CharField(blank=True, max_length=200, null=True)),
                ('Address2', models.CharField(blank=True, max_length=200, null=True)),
                ('PostOffice', models.CharField(blank=True, max_length=30, null=True)),
                ('District', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.district')),
                ('Division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.division')),
                ('PostalCode', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.postcode')),
                ('Upazila', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.upazila')),
            ],
        ),
    ]
