# Generated by Django 2.1.5 on 2019-02-28 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20190221_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finance',
            old_name='acces_points_count',
            new_name='access_point_count',
        ),
    ]
