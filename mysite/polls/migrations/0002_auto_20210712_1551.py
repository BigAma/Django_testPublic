# Generated by Django 3.1.5 on 2021-07-12 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='question_label',
            field=models.CharField(default=datetime.datetime(2021, 7, 12, 12, 51, 17, 779295, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
