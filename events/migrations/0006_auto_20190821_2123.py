# Generated by Django 2.2.4 on 2019-08-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190821_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(),
        ),
    ]
