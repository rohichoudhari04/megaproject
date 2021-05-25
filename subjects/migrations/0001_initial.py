# Generated by Django 3.1.5 on 2021-05-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='pics/')),
                ('date_posted', models.DateField(blank=True)),
                ('last_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='notes/pdfs/')),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('Roll_no', models.CharField(max_length=10)),
                ('pdf', models.FileField(upload_to='notes/stu_pdfs/')),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%y')),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
