# Generated by Django 2.1.5 on 2019-03-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0022_auto_20190308_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layertable',
            name='input',
        ),
        migrations.AddField(
            model_name='layertable',
            name='sub_category',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
