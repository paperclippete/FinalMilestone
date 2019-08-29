# Generated by Django 2.2.4 on 2019-08-29 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190829_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_time',
            new_name='event_time_begins',
        ),
        migrations.AddField(
            model_name='event',
            name='event_time_ends',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
