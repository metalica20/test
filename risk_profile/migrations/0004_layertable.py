# Generated by Django 2.1.5 on 2019-03-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0003_auto_20190306_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layer_name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('layer_tbl', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('layer_icon', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('layer_cat', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('isGeoserver', models.BooleanField(blank=True, default=True, null=True)),
                ('public', models.BooleanField(blank=True, default=True, null=True)),
                ('visibility_level', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('layer_type', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('hazard', models.CharField(choices=[('flood', 'Flood'), ('landslide', 'Landslide'), ('fire', 'Fire'), ('earthquake', 'Earthquake')], max_length=35)),
            ],
        ),
    ]
