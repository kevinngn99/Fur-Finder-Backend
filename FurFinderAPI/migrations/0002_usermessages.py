# Generated by Django 3.0.6 on 2020-07-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurFinderAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.TextField(default='')),
                ('user2', models.TextField(default='')),
                ('threadID', models.TextField(default='')),
                ('message', models.TextField(default='')),
            ],
        ),
    ]
