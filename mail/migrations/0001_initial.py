# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=280)),
                ('content', models.TextField()),
            ],
        ),
    ]
