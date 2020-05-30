# Generated by Django 3.0.6 on 2020-05-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('age', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('dob', models.CharField(max_length=128)),
            ],
        ),
    ]
