# Generated by Django 3.0.3 on 2021-09-19 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 19, 58, 0, 706024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 19, 58, 0, 705538, tzinfo=utc)),
        ),
    ]
