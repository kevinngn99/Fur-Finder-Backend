# Generated by Django 3.0.6 on 2020-06-25 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurFinderAPI', '0002_auto_20200612_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='FidoFinder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
                ('petid', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='HelpingLostPets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('age', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='LostMyDoggie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('zip', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PawBoost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('petid', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PetKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('age', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TabbyTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
                ('petid', models.CharField(max_length=128)),
            ],
        ),
    ]
