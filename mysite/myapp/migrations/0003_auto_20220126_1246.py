# Generated by Django 3.1.7 on 2022-01-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220126_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.CharField(default='', max_length=100),
        ),
    ]
