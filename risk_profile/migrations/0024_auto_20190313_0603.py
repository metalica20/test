# Generated by Django 2.1.5 on 2019-03-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0023_auto_20190308_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='layertable',
            name='geoserver_url',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='layertable',
            name='geoserver_workspace',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
