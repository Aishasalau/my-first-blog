# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-10 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 10, 17, 7, 15, 53189, tzinfo=utc)),
        ),
    ]
