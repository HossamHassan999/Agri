# Generated by Django 5.1 on 2024-09-01 11:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandPlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('recorded_area', models.CharField(max_length=255)),
                ('parcel_code', models.IntegerField()),
                ('crop_type', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Land_plots',
        ),
    ]
