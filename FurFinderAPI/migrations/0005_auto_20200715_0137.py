# Generated by Django 3.0.6 on 2020-07-15 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurFinderAPI', '0004_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.TextField(default='Name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.TextField(default='Password'),
        ),
        migrations.AlterField(
            model_name='account',
            name='password2',
            field=models.TextField(default='Password2'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.TextField(default='Username'),
        ),
    ]
