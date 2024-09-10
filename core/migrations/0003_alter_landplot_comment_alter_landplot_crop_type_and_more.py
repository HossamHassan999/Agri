# Generated by Django 5.1 on 2024-09-02 06:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_landplot_delete_land_plots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landplot',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='crop_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='owner_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='parcel_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='recorded_area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
