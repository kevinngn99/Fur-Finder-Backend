# Generated by Django 3.0.6 on 2020-07-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurFinderAPI', '0002_auto_20200717_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimage',
            name='image',
            field=models.ImageField(blank=None, upload_to='images/'),
        ),
    ]