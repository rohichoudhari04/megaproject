# Generated by Django 3.1.5 on 2021-02-27 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20210227_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='subject',
            field=models.CharField(default=datetime.datetime(2021, 2, 27, 17, 51, 9, 30498, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]