# Generated by Django 3.1.5 on 2021-02-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20210227_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='title',
        ),
    ]
