# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20161222_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('cp', models.CharField(max_length=5)),
                ('country_code', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='cookingcourse',
            name='pupils',
            field=models.ManyToManyField(to='course.Pupil'),
        ),
    ]
