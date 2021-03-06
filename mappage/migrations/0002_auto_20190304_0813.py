# Generated by Django 2.1.5 on 2019-03-04 08:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='latitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='longitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='latitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='longitude',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='location_point',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, default=None, null=True, srid=4326),
        ),
    ]
