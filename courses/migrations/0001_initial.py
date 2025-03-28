# Generated by Django 5.1.6 on 2025-03-25 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('grade', models.CharField(max_length=1)),
                ('remark', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('coursecontent', models.TextField()),
                ('student', models.ManyToManyField(to='users.studentprofile')),
                ('results', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.results')),
            ],
        ),
    ]
