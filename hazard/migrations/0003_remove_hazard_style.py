# Generated by Django 2.1.5 on 2019-02-25 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hazard', '0002_auto_20190225_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazard',
            name='style',
        ),
    ]
