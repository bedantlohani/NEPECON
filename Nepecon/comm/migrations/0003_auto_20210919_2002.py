# Generated by Django 3.0.3 on 2021-09-19 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0002_auto_20210919_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 20, 2, 2, 602772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 20, 2, 2, 602290, tzinfo=utc)),
        ),
    ]