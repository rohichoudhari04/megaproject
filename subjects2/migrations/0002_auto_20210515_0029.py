# Generated by Django 3.1.5 on 2021-05-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment2',
            name='date_posted',
            field=models.DateField(blank=True, help_text='m/d/Y'),
        ),
        migrations.AlterField(
            model_name='assignment2',
            name='last_date',
            field=models.DateField(blank=True, help_text='m/d/Y'),
        ),
        migrations.AlterField(
            model_name='note2',
            name='date',
            field=models.DateField(blank=True, help_text='m/d/Y'),
        ),
        migrations.AlterField(
            model_name='student_assign2',
            name='date',
            field=models.DateField(blank=True, help_text='m/d/Y'),
        ),
        migrations.AlterField(
            model_name='video2',
            name='date',
            field=models.DateField(blank=True, help_text='m/d/Y'),
        ),
    ]