# Generated by Django 3.0.6 on 2020-07-15 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurFinderAPI', '0004_auto_20200714_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='state',
        ),
        migrations.AddField(
            model_name='pet',
            name='color',
            field=models.TextField(default='Color'),
        ),
        migrations.AddField(
            model_name='pet',
            name='petid',
            field=models.TextField(default='PetID'),
        ),
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.TextField(default='Status'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.TextField(default='Age'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.TextField(default='Breed'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='date',
            field=models.TextField(default='Date'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.TextField(default='Gender'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='location',
            field=models.TextField(default='Location'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.TextField(default='Name'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.TextField(default='Size'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='zip',
            field=models.TextField(default='Zip'),
        ),
    ]
